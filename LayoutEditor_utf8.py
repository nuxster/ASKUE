#!/usr/bin/env python3
# coding: UTF-8

import time
import sys
import os
import datetime
import lxml.etree as et
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
# GUI
from gui import Ui_MainWindow

class LEMainWindow(QtWidgets.QMainWindow):
    '''
    Основной класс
    '''
    def __init__(self):
        super(LEMainWindow, self).__init__()
        # Некоммерческие присоединения
        self.non_profit_measuringpoints = []
        #  Состояние макета (редактировался?)
        self.edited_by_template = False
        #
        self.ui = Ui_MainWindow()
        self.setup_ui()


    def setup_ui(self):
        '''
        Инициализация элементов графического интерфейса.
        Установка значений по умолчанию.
        '''
        self.ui.setupUi(self)
        # Строка меню
        self.init_menu()
        # treeView
        self.template_data_model = QtGui.QStandardItemModel()
        # self.template_data_model.setColumnCount(9)
        self.header_labels = ['Точка учета', 'Начало', 'Окончание', 'Статус', 'A+', 'A-', 'R+', 'R-']
        self.template_data_model.setHorizontalHeaderLabels(self.header_labels)
        self.ui.templateDataTree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.templateDataTree.setAlternatingRowColors(True)
        self.ui.templateDataTree.setAllColumnsShowFocus(True)
        self.ui.templateDataTree.setMinimumWidth(640)
        self.ui.templateDataTree.setMinimumHeight(480)
        self.ui.templateDataTree.setModel(self.template_data_model)
        self.ui.templateDataTree.selectionModel().selectionChanged.connect(self.treeview_select_row)
        # Название вкладок
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_1), 'Статус')
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_2), 'Объём')
        # Общая область
        self.ui.label_selected_measuringpoint.setText('Присоединение')
        # Комбобоксы выбора интервала
        self.ui.startTime_label.setText('Начало:')
        self.ui.startPeriod_comboBox.setStyleSheet('combobox-popup: 0;')
        self.ui.endTime_label.setText('Окончание:')
        self.ui.endPeriod_comboBox.setStyleSheet('combobox-popup: 0;')
        # Вкладка 'Статус'
        # Выбор типа присоединения
        self.ui.measuringpointType_label.setText('Присоединения:')
        self.ui.comboBox_measuringpoint_type.addItems(('', 'Все некоммерч.', 'Все'))
        # Инициализация интервалов
        self.populate_period(init=True)
        # Реинициализация времемени окончания после выбора времени начала
        self.ui.startPeriod_comboBox.currentIndexChanged.connect(lambda: self.populate_period(
            start_time=self.ui.startPeriod_comboBox.currentText()))
        # Комбобокс выбора флага
        self.ui.selectFlag_label.setText('Флаг:')
        self.ui.comboBox_select_flag.addItems(('0', '1'))
        # Вкладка 'Объем'
        # Инициализация чекбоксов по каналам
        self.ui.checkBox_save_a_plus.setText('Только получасовка')
        self.ui.checkBox_save_a_plus.setChecked(True)
        self.ui.checkBox_save_a_minus.setText('Только получасовка')
        self.ui.checkBox_save_a_minus.setChecked(True)
        self.ui.checkBox_save_r_plus.setText('Только получасовка')
        self.ui.checkBox_save_r_plus.setChecked(True)
        self.ui.checkBox_save_r_minus.setText('Только получасовка')
        self.ui.checkBox_save_r_minus.setChecked(True)
        #
        self.ui.label_a_plus.setText('Активная приём (A+)')
        self.ui.label_a_minus.setText('Активная отдача (A-)')
        self.ui.label_r_plus.setText('Реактивная приём (R+)')
        self.ui.label_r_minus.setText('Реактивная отдача (R-)')
        # Кнопка применить
        self.ui.pushButton_apply.setText('Применить')
        # По умолчанию кнопка не активна
        self.ui.pushButton_apply.setEnabled(False)
        self.ui.pushButton_apply.clicked.connect(self.clicked_pushbutton_apply)
        self.open_xml()


    def init_menu(self):
        '''
        Инициализация строки меню.
        Наполнение пунктов меню, привязка действий к функциям, задание параметров по умолчанию.
        '''
        # Меню "Файл"
        filemenu = self.ui.menubar.addMenu('Файл')
        self.open_xml_action = QtWidgets.QAction('Открыть макет', self)
        self.open_xml_action.triggered.connect(self.open_xml)
        filemenu.addAction(self.open_xml_action)

        self.save_xml_action = QtWidgets.QAction('Сохранить макет', self)
        self.save_xml_action.triggered.connect(self.save_xml)
        filemenu.addAction(self.save_xml_action)
        self.save_xml_action.setEnabled(False)

        self.exit_action = QtWidgets.QAction('Выход', self)
        self.exit_action.triggered.connect(QtWidgets.qApp.quit)
        filemenu.addAction(self.exit_action)


    def treeview_select_row(self):
        '''
        Действия при выборе строки в treeview.
        '''
        indexes = self.ui.templateDataTree.selectedIndexes()
        measuringpoint = indexes[0].parent().data(QtCore.Qt.DisplayRole) or indexes[0].data(QtCore.Qt.DisplayRole)
        self.populate_comboBox_selected_measuringpoint(current_item=measuringpoint)
        try:
            # Вывод объемов на редактирование по каналам
            self.ui.lineEdit_a_plus.setText(indexes[5].data(QtCore.Qt.DisplayRole))
            self.ui.lineEdit_a_minus.setText(indexes[6].data(QtCore.Qt.DisplayRole))
            self.ui.lineEdit_r_plus.setText(indexes[7].data(QtCore.Qt.DisplayRole))
            self.ui.lineEdit_r_minus.setText(indexes[8].data(QtCore.Qt.DisplayRole))
            # Установка интервала в combobox'ах в соответствии с выбором в treeview
            self.populate_period(start_time=':'.join((indexes[1].data(QtCore.Qt.DisplayRole)[:2], indexes[1].data(QtCore.Qt.DisplayRole)[2:])))
        except IndexError:
            pass


    def populate_period(self, init=False, start_time="00:00"):
        '''
        Инициализация combobox'ов с выбором интервалов.
        Генерирует наполнение в зависимости от выбора начального значения.
        Контролирует корректность выбранного периода.
        '''
        # Выполняется при заданном начальном времени
        if not init:
            self.ui.startPeriod_comboBox.setCurrentIndex(self.ui.startPeriod_comboBox.findText(start_time))
        # Преобразование стартового значения для генерации значений периода окончания
        start_time = int(datetime.timedelta(hours=int(start_time.split(':')[0]),
            minutes=int(start_time.split(':')[1])).seconds/60)
        if not init:
            # Сдвиг на 30 минут для врмени окончания периода
            start_time += 30 
        # Генератор списка периода по получасовкам
        period_generator = [":".join((h.zfill(2), m)) for h, m in iter(
                (lambda i: [str(datetime.timedelta(minutes=x))[:-3].split(':') for x in i] )
                    (i for i in range(start_time, 1411, 30)))]
        # Список стартовых значений генерируется только при запуске программы
        if init:
            #init введена из-за падения Qt при реинициализации startPriod_comboBox (bug)
            self.ui.startPeriod_comboBox.addItems(period_generator)
        self.ui.endPeriod_comboBox.clear()
        self.ui.endPeriod_comboBox.addItems(period_generator)
        # Всегда должно быть значение конца суток
        self.ui.endPeriod_comboBox.addItem('00:00')


    def populate_comboBox_selected_measuringpoint(self, current_item=0, measuringpoints=0):
        '''
        Заполнение combobox'а присоединениями из текущего макета.
        '''
        if measuringpoints:
            self.ui.comboBox_selected_measuringpoint.clear()
            self.ui.comboBox_selected_measuringpoint.addItems(measuringpoints)
        else:
            self.ui.comboBox_selected_measuringpoint.setCurrentIndex(self.ui.comboBox_selected_measuringpoint.findText(current_item))


    def open_xml(self):
        '''
        Метод открытия шаблона для обработки.
        '''
        if self.template_data_model.rowCount() > 0:
            self.send_message('Сохрани макет', 1)
            self.template_data_model.clear()
        # self.templateXMLfile, _ = QtWidgets.QFileDialog().getOpenFileName(self, 
        #     'Открыть макет', os.path.dirname(os.path.realpath(__file__)), 'Макет XML (*xml)')
        # self.templateXMLfile = "/home/nuxster/Files/git/ASKUE/Макеты/80020_7841312071_20200205_59409_5100003400.xml"
        self.templateXMLfile = "/home/nuxster/Files/git/ASKUE/80020_7841312071_20190624_45254_5100000200.xml"
        if os.path.exists(self.templateXMLfile):
            self.tree = et.parse(self.templateXMLfile)
            self.xml_to_treeview(self.tree.getroot())
            # Имя файла-шаблона в сообщении строки состояния
            self.ui.statusbar.showMessage(f"Макет: {self.templateXMLfile.split(os.sep)[-1:][0]}")


    def save_xml(self):
        '''
        Сохранение исправленного шаблона.
        '''
        savefile, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить макет', self.templateXMLfile, 'Макет XML (*xml)')
        try:
            self.tree.write(savefile, encoding='windows-1251')
        except Exception as exception_event:
            self.message("Ошибка записи макета: {0}".format(exception_event))


    def xml_to_treeview(self, root):
        '''
        Заполнение модели данных для treeview
        '''
        self.template_data_model.clear()
        self.template_data_model.setHorizontalHeaderLabels(self.header_labels)
        # Временный список для некоммерческих присоединений
        non_profit_measuringpoints_list = []
        measuringpoint_list = []
        for child in root.iterfind('.//'):
            if child.tag == 'area':
                for subchild in child:
                    # Точка учета
                    if subchild.tag == 'measuringpoint':
                        measuringpoint = QtGui.QStandardItem(subchild.attrib['name'])
                        measuringpoint_list.append(subchild.attrib['name'])
                        self.template_data_model.appendRow(measuringpoint)
                        # Канал
                        # Счетчик колонок для отображения объемов по каналам
                        column_counter = 3
                        for measuringchannel_in in subchild:
                            # Колонка объемов по канала
                            measuringchannel_volume = []
                            # С каждым проходом добавляем колонку
                            column_counter += 1
                            if measuringchannel_in.tag == 'measuringchannel':
                                # Период, флаг, объем
                                for period_in in measuringchannel_in:
                                    # Период (заполняем по первому каналу)
                                    if period_in.tag == 'period':
                                        if measuringchannel_in.attrib['code'] == '01':
                                            period = [QtGui.QStandardItem(),
                                                QtGui.QStandardItem(period_in.attrib['start']),
                                                QtGui.QStandardItem(period_in.attrib['end']),]
                                            # Флаг по первому каналу
                                            for value_in in period_in:
                                                try:
                                                    period.append(QtGui.QStandardItem(value_in.attrib['status']),)
                                                    non_profit_measuringpoints_list.append(measuringpoint.text())
                                                    # Окрашиваем ячейки с некоммерческой информацией
                                                    [i.setBackground(QtGui.QColor('#F15A24')) for i in [measuringpoint,] + period]
                                                except KeyError:
                                                    period.append(QtGui.QStandardItem('0'),)
                                                # Объем по первому каналу
                                                period.append(QtGui.QStandardItem(value_in.text),)
                                                measuringpoint.appendRow(period)
                                        # Объемы по остальным каналам
                                        for value_in in period_in:
                                            measuringchannel_volume.append(QtGui.QStandardItem(value_in.text))
                            measuringpoint.insertColumn(column_counter, measuringchannel_volume)
        # Заполнение combobox'а присоединениями из текущего макета 
        self.populate_comboBox_selected_measuringpoint(measuringpoints=measuringpoint_list)
        # Удаление лишнего из списка некоммерческих присоединений
        self.non_profit_measuringpoints = set(non_profit_measuringpoints_list)
        # Активировать пункт меню сохраняющий макет
        self.save_xml_action.setEnabled(True)
        # Активировать кнопку 'Применить'
        self.ui.pushButton_apply.setEnabled(True)


    def change_status(self, measuringchannel, start, end, flag):
        '''
        Функция меняет флаг в указанном интервале для каждого измерительного канала.
        '''
        processing_interval = False
        for period in measuringchannel:
            if (period.attrib['start'] == start):
                processing_interval = True
            # Обработка временного интервала
            if processing_interval:
                for value in period:
                    if flag == 0:
                        try:
                            del value.attrib['status']
                        except KeyError:
                            pass
                    else:
                        value.set('status', "1")
            if period.attrib['end'] == end:
                return measuringchannel


    def adjustment_volume(self, measuringpoint, measuringchannels_value, start, end):
        '''
        '''
        root = self.tree.getroot()
        for child in root.iterfind('.//'):
            if (child.tag == 'measuringpoint') and (child.attrib['name'] == measuringpoint):
                print(child.attrib['name'])
                # for i in measuringchannels_value:
                #     print([measuringchannel for measuringchannel in child if measuringchannel.attrib['code'] == i])





    def clicked_pushbutton_apply(self):
        '''
        Действия по нажатию кнопки "Применить".
        '''
        if self.template_data_model.rowCount() < 1:
            self.send_message("Требуется загрузить макет.")
            return()
        start = "".join(self.ui.startPeriod_comboBox.currentText().split(':'))
        end = "".join(self.ui.endPeriod_comboBox.currentText().split(':'))
        flag = int(self.ui.comboBox_select_flag.currentText())
        measuringpoint = self.ui.comboBox_selected_measuringpoint.currentText()
        root = self.tree.getroot()
        # Действия для вкладки "Статус"
        if self.ui.tabWidget.currentIndex() == 0:
            # Если присоединение было выбрано вручную 
            if self.ui.comboBox_measuringpoint_type.currentIndex() == 0:
                for child in root.iterfind('.//'):
                    if (child.tag == 'measuringpoint') and (child.attrib['name'] == self.ui.comboBox_selected_measuringpoint.currentText()):
                        for measuringchannel in child:
                            measuringchannel = self.change_status(measuringchannel, start, end, flag)
            # Для всех некоммерческих значений
            elif self.ui.comboBox_measuringpoint_type.currentIndex() == 1:
                for measuringpoint_in in self.non_profit_measuringpoints:
                    for measuringpoint in root.findall("./area/measuringpoint"):
                        if measuringpoint.attrib['name'] == measuringpoint_in:
                            for measuringchannel in measuringpoint:
                                measuringchannel = self.change_status(measuringchannel, start, end, flag)
            # Для всего шаблона
            elif self.ui.comboBox_measuringpoint_type.currentIndex() == 2:
                for child in root.iterfind('.//'):
                    if (child.tag == 'measuringpoint'):
                        for measuringchannel in child:
                            measuringchannel = self.change_status(measuringchannel, start, end, flag)
        # Действия для вкладки "Объем"
        elif self.ui.tabWidget.currentIndex() == 1:
            measuringchannels_value = {
                "01":(self.ui.lineEdit_a_plus.text(), self.ui.checkBox_save_a_plus.isChecked()),
                "02":(self.ui.lineEdit_a_minus.text(), self.ui.checkBox_save_a_minus.isChecked()),
                "03":(self.ui.lineEdit_r_plus.text(), self.ui.checkBox_save_r_plus.isChecked()),
                "04":(self.ui.lineEdit_r_minus.text(), self.ui.checkBox_save_r_minus.isChecked())
            }
            self.adjustment_volume(measuringpoint, measuringchannels_value, start, end)
        
        # Перезагрузить treeview
        self.xml_to_treeview(root)


    def send_message(self, msg, save=0):
        '''
        Вывод сообщений и диалогов.
        '''
        massage_box = QtWidgets.QMessageBox()
        if save == 1:
            btn = massage_box.question(self, "Сообщение", msg, QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        else:
            btn = massage_box.question(self, "Сообщение", msg, QtWidgets.QMessageBox.Ok)
        if btn == QtWidgets.QMessageBox.Yes:
            self.save_xml()
        else:
            pass


def main():
    '''
    Создание экземпляра окна приложения и его запуск.
    '''
    app = QApplication(sys.argv)
    window = LEMainWindow()
    window.setWindowTitle('Редактор макетов')
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
