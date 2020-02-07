#!/usr/bin/env python3
# coding: utf-8


import sys
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
        # Название вкладок
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_1), "Статус")
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_2), "Объём")
        
        # Вкладка "Статус"
        self.ui.chbx_for_all_bad_joining.setText("Для всех некомерч.")
        self.ui.chbx_for_all_bad_joining.setChecked(True)
        self.ui.chbx_for_all_joining.setText("Для всех")
        self.ui.chbx_for_all_bad_joining.stateChanged.connect(lambda: True if 
            (self.ui.chbx_for_all_bad_joining.isChecked() == False) else self.ui.chbx_for_all_joining.setChecked(False))
        self.ui.chbx_for_all_joining.stateChanged.connect(lambda: True if 
            (self.ui.chbx_for_all_joining.isChecked() == False) else self.ui.chbx_for_all_bad_joining.setChecked(False))
        # Комбобоксы выбора интервала
        self.ui.startTime_label.setText("Начало:")
        self.ui.endTime_label.setText("Окончание:")

        # Комбобокс выбора флага
        self.ui.comboBox_select_flag.addItem('Флаг 0', 0)
        self.ui.comboBox_select_flag.addItem('Флаг 1', 1)

        # Кнопка применить
        self.ui.pushButton_apply.setText("Применить")

def main():
    app = QApplication(sys.argv)
    form = LE_MainWindow()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
