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
        self.ui = Ui_MainWindow()
        self.setup_ui()
        # Список некоммерческих присоединений
        self.non_profit_connections = []
        #  Состояние макета (редактировался?)
        self.edited_by_template = False


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
        self.template_data_model.setColumnCount(1)
        self.ui.templateDataTree.header().hide()
        self.ui.templateDataTree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.templateDataTree.setModel(self.template_data_model)
        # Название вкладок
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_1), 'Статус')
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_2), 'Объём')
        # Вкладка 'Статус'
        # Выбор типа присоединения
        self.ui.connectionType_label.setText('Присоединения:')
        self.ui.comboBox_connection_type.addItems(('', 'Все некоммерч.', 'Все'))
        # Комбобоксы выбора интервала
        self.ui.startTime_label.setText('Начало:')
        self.ui.startPeriod_comboBox.setStyleSheet('combobox-popup: 0;')
        self.ui.endTime_label.setText('Окончание:')
        self.ui.endPeriod_comboBox.setStyleSheet('combobox-popup: 0;')
        # Инициализация интервалов
        self.set_period(init=True)
        # Реинициализация времемени окончания после выбора времени начала
        self.ui.startPeriod_comboBox.currentIndexChanged.connect(lambda: self.set_period(
            start_Time=self.ui.startPeriod_comboBox.currentText()))
        # Комбобокс выбора флага
        self.ui.selectFlag_label.setText('Флаг:')
        self.ui.comboBox_select_flag.addItems(('0', '1'))

        # 

        # Кнопка применить
        self.ui.pushButton_apply.setText('Применить')
        # По умолчанию кнопка не активна
        self.ui.pushButton_apply.setEnabled(False)
        self.ui.pushButton_apply.clicked.connect(self.clicked_pushbutton_apply)


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


    def set_period(self, init=False, start_Time="00:00"):
        '''
        Инициализация combobox'ов с выбором интервалов.
        Генерирует наполнение в зависимости от выбора начального значения.
        Контролирует корректность выбранного периода.
        '''
        # Преобразование стартового значения для генерации значений периода окончания
        start_Time = int(datetime.timedelta(hours=int(start_Time.split(':')[0]),
            minutes=int(start_Time.split(':')[1])).seconds/60)
        if not init:
            # Сдвиг на 30 минут для врмени окончания периода
            start_Time += 30 
        # Генератор списка периода по получасовкам
        period_generator = [":".join((h.zfill(2), m)) for h, m in iter(
                (lambda i: [str(datetime.timedelta(minutes=x))[:-3].split(':') for x in i] )
                    (i for i in range(start_Time, 1411, 30)))]
        # Список стартовых значений генерируется только при запуске программы
        if init:
            #init введена из-за падения Qt при реинициализации startPriod_comboBox (bug)
            self.ui.startPeriod_comboBox.addItems(period_generator)
        self.ui.endPeriod_comboBox.clear()
        self.ui.endPeriod_comboBox.addItems(period_generator)
        # Всегда должно быть значение конца суток
        self.ui.endPeriod_comboBox.addItem('00:00')

    
    def open_xml(self):
        '''
        Метод открытия шаблона для обработки.
        '''
        if self.template_data_model.rowCount() > 0:
            self.send_message('Сохрани макет', 1)
            self.template_data_model.clear()
        self.templateXMLfile, _ = QtWidgets.QFileDialog().getOpenFileName(self, 
            'Открыть макет', os.path.dirname(os.path.realpath(__file__)), 'Макет XML (*xml)')
        if os.path.exists(self.templateXMLfile):
            self.tree = et.parse(self.templateXMLfile)
            self.xml_to_treeview(self.tree.getroot())
            # Имя файла-шаблона в ообщении строки состояния
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
        root_item = QtGui.QStandardItem()
        measuringpoint = QtGui.QStandardItem()
        measuringpoint_item = ''
        measuringpoint_list = []
        measuringchannel = QtGui.QStandardItem()
        period = QtGui.QStandardItem()
        for child in root.iterfind('.//'):
            if child.tag == 'area':
                for subchild in child:
                    if subchild.tag == 'inn':
                        root_item = QtGui.QStandardItem(subchild.text)
                        self.template_data_model.appendRow(root_item)
            #
            if child.tag == 'measuringpoint':
                measuringpoint = QtGui.QStandardItem(child.attrib['name'])
                root_item.appendRow(measuringpoint)
                measuringpoint_item = child.attrib['name']
            #
            if child.tag == 'measuringchannel':
                measuringchannel = QtGui.QStandardItem(child.attrib['desc'])
                measuringpoint.appendRow(measuringchannel)
            #
            if child.tag == 'period':
                period = QtGui.QStandardItem(str(child.attrib['start']+' - '+child.attrib['end']+' --> [ '+child[0].text+' ]'))
                measuringchannel.appendRow(period)
            #
            if child.tag == 'value':
                try:
                    period.appendRow(QtGui.QStandardItem(child.text+' : '+child.attrib['status']))
                except KeyError:
                    period.appendRow(QtGui.QStandardItem(child.text))
                try:
                    if child.attrib['status'] == '1':
                        measuringpoint.setBackground(QtGui.QColor('#F15A24'))
                        measuringpoint_list.append(measuringpoint_item)
                        measuringchannel.setBackground(QtGui.QColor('#F15A24'))
                        period.setBackground(QtGui.QColor('#F15A24'))
                except KeyError:
                    pass
        self.non_profit_connections = set(measuringpoint_list)
        # Раскрыть корневой элемент в treeView
        self.ui.templateDataTree.setExpanded(self.template_data_model.index(0, 0), True)
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
        root = self.tree.getroot()
        # Если присоединение было выбрано в TreeView
        if self.ui.comboBox_connection_type.currentIndex() == 0:
            try:
                treeview_selected = self.template_data_model.itemData(
                    self.ui.templateDataTree.currentIndex())[0]
            except KeyError:
                self.send_message('Повторите выбор элемента.')
            for child in root.iterfind('.//'):
                if (child.tag == 'measuringpoint') and (child.attrib['name'] == treeview_selected):
                    for measuringchannel in child:
                        measuringchannel = self.change_status(measuringchannel, start, end, flag)
        # Для всех некоммерческих значений
        elif self.ui.comboBox_connection_type.currentIndex() == 1:
            for connection in self.non_profit_connections:
                for measuringpoint in root.findall("./area/measuringpoint"):
                    if measuringpoint.attrib['name'] == connection:
                        for measuringchannel in measuringpoint:
                            measuringchannel = self.change_status(measuringchannel, start, end, flag)
        # Для всего шаблона
        elif self.ui.comboBox_connection_type.currentIndex() == 2:
            for child in root.iterfind('.//'):
                if (child.tag == 'measuringpoint'):
                    for measuringchannel in child:
                        measuringchannel = self.change_status(measuringchannel, start, end, flag)
        self.template_data_model.clear()
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
