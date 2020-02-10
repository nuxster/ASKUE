#!/usr/bin/env python3
# coding: utf-8


import sys
import os
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
# GUI
from gui import Ui_MainWindow


try:
    import xml.etree.cElementTree as et
except:
    import xml.etree.ElementTree as et


class LE_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LE_MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.setupUi()

    def setupUi(self):
        self.ui.setupUi(self)
        
        # Строка меню
        self.initMenu()

        # treeView
        self.templateDataModel = QtGui.QStandardItemModel()
        self.templateDataModel.setColumnCount(1)
        self.ui.templateDataTree.header().hide()
        self.ui.templateDataTree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.templateDataTree.setModel(self.templateDataModel)

        
        # Название вкладок
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_1), 'Статус')
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_2), 'Объём')
        
        
        # Вкладка 'Статус'

        # Выбор типа присоединения
        self.ui.connectionType_label.setText('Присоединения:')
        self.ui.comboBox_connection_type.addItems(('', 'Все некомерч.', 'Все'))
        

        # Комбобоксы выбора интервала
        self.ui.startTime_label.setText('Начало:')
        self.ui.startPeriod_comboBox.setStyleSheet('combobox-popup: 0;')
        self.ui.endTime_label.setText('Окончание:')
        self.ui.endPeriod_comboBox.setStyleSheet('combobox-popup: 0;')
                
        # Инициализация интервалов
        self.setPeriod()

        # Реинициализация времемени окончания после выбора времени начала
        self.ui.startPeriod_comboBox.currentIndexChanged.connect(lambda: self.setPeriod(
            startTime=self.ui.startPeriod_comboBox.currentText()))
        
        
        # Комбобокс выбора флага
        self.ui.selectFlag_label.setText('Флаг:')
        self.ui.comboBox_select_flag.addItems(('0', '1'))
        
        # Кнопка применить
        self.ui.pushButton_apply.setText('Применить')
        # self.ui.pushButton_apply.setEnabled(False)
        self.ui.pushButton_apply.clicked.connect(lambda: self.clicked_pushButton_apply())
    
    # Инициализация пунктов строки меню
    def initMenu(self):
        '''
        Инициализация строки меню.
        Наполнение пунктов меню, привязка действий к функциям, задание параметров по умолчанию.
        '''
        filemenu = self.ui.menubar.addMenu('Файл')
        self.openXmlAction = QtWidgets.QAction('Открыть макет', self)
        self.openXmlAction.triggered.connect(self.openXml)
        filemenu.addAction(self.openXmlAction)

        self.saveXmlAction = QtWidgets.QAction('Сохранить макет', self)
        self.saveXmlAction.triggered.connect(self.saveXml)
        filemenu.addAction(self.saveXmlAction)
        self.saveXmlAction.setEnabled(False)

        self.exitAction = QtWidgets.QAction('Выход', self)
        self.exitAction.triggered.connect(QtWidgets.qApp.quit)
        filemenu.addAction(self.exitAction)        


    # Инициализация интервалов
    def setPeriod(self, startTime='00:00'):
        '''
        Инициализация combobox'ов с выбором интервалов.
        Генерирует наполнение в зависимости от выбора начального значения.
        Контролирует корректность выбранного периода.
        '''
        # Список стартовых значений генерируется только при запуске программы
        if startTime == '00:00':
            self.ui.startPeriod_comboBox.addItems([":".join((h.zfill(2), m)) for h, m in iter(
                (lambda i: [str(datetime.timedelta(minutes=x))[:-3].split(':') for x in i] )(i for i in range(0, 1411 ,30)))])
        
        # Преобразование стартового значения для генерации значений периода окончания
        startTime = int(datetime.timedelta(hours=int(startTime.split(':')[0]), minutes=int(startTime.split(':')[1])).seconds/60)
        
        self.ui.endPeriod_comboBox.clear()
        
        self.ui.endPeriod_comboBox.addItems([":".join((h.zfill(2), m)) for h, m in iter(
                (lambda i: [str(datetime.timedelta(minutes=x))[:-3].split(':') for x in i] )(i for i in range(startTime+30, 1411 ,30)))])
        
        # Всегда должно быть значение конца суток
        self.ui.endPeriod_comboBox.addItem('00:00')


    def openXml(self):
        # if self.templateDataModel.rowCount() > 0:
        #     self.message('Сохрани макет', 1)
        #     self.templateDataModel.clear()
        self.templateXMLfile, _ = QtWidgets.QFileDialog().getOpenFileName(self, 
            'Открыть макет', os.path.dirname(os.path.realpath(__file__)), 'Макет XML (*xml)')
        # self.ui.statusbar.showMessage(self.templateXMLfile)
        if os.path.exists(self.templateXMLfile):
            self.tree = et.ElementTree(file=self.templateXMLfile)
            self.xmlToTreeView(self.tree.getroot())
        # сохранение 'шапки' макета 
        # if not self.saveHeader():
        # if os.path.exists(self.templateXMLfile):
        #         self.tree.__init__(file=self.templateXMLfile)
        #         self.xmlToTreeView(self.tree.getroot())


    def saveXml(self):
        pass


    # Заполнение модели данных для treeview
    def xmlToTreeView(self, root):
        # self.bad_joining_comboboxModel.clear()
        rootItem = QtGui.QStandardItem()
        measuringpoint = QtGui.QStandardItem()
        measuringpoint_item = ''
        measuringpoint_list = []
        measuringchannel = QtGui.QStandardItem()
        period = QtGui.QStandardItem()
        for child in root.iterfind('.//'):
            if child.tag == 'area':
                for subchild in child:
                    if subchild.tag == 'inn':
                        rootItem = QtGui.QStandardItem(subchild.text)
                        self.templateDataModel.appendRow(rootItem)
            #
            if child.tag == 'measuringpoint':
                measuringpoint = QtGui.QStandardItem(child.attrib['name'])
                rootItem.appendRow(measuringpoint)
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
                except:
                    period.appendRow(QtGui.QStandardItem(child.text))
                try:
                    child.attrib['status'] == '1'
                    measuringpoint.setBackground(QtGui.QColor('#F15A24'))
                    measuringpoint_list.append(measuringpoint_item)
                    measuringchannel.setBackground(QtGui.QColor('#F15A24'))
                    period.setBackground(QtGui.QColor('#F15A24'))
                except:
                    pass
        bad_joining_combobox = []            
        for joining in measuringpoint_list:
            if joining not in bad_joining_combobox:
                bad_joining_combobox.append(joining)
                # self.bad_joining_comboboxModel.appendRow(QtGui.QStandardItem(joining))
        # Раскрыть корневой элемент в treeView
        self.ui.templateDataTree.setExpanded(self.templateDataModel.index(0, 0), True)
        # Активировать пункт меню сохраняющий макет
        self.saveXmlAction.setEnabled(True)
        # Активировать кнопку 'Применить'
        self.ui.pushButton_apply.setEnabled(True)


    def clicked_pushButton_apply(self):
        print(self.templateDataModel.itemData(self.ui.templateDataTree.currentIndex())[0])


def main():
    app = QApplication(sys.argv)
    form = LE_MainWindow()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
