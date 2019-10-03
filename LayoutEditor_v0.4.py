# coding: windows-1251

import sys
from os import path
from datetime import date, datetime, time, timedelta
from PyQt5 import QtWidgets, QtGui, QtCore
try:
    import xml.etree.cElementTree as et
except:
    import xml.etree.ElementTree as et

class MyWindows(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # ���� � xml-������
        self.templateXMLfile = None
        # ��� �������� ����� ������ � ����������� ������ ��� ���������� ���������
        self.header = []
        #
        self.tree = et.ElementTree()
        # ������ ������
        self.templateDataModel = QtGui.QStandardItemModel()
        self.templateDataModel.setColumnCount(1)
        # ������ ����
        self.main_menu = self.menuBar()
        self.openXmlAction = QtWidgets.QAction('&������� �����', self)
        self.saveXmlAction = QtWidgets.QAction('&��������� �����', self)
        self.exitAction = QtWidgets.QAction('&�����', self)
        #
        self.templateDataTree = QtWidgets.QTreeView()
        self.templateDataTree.header().hide()
        self.templateDataTree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.templateDataTree.setModel(self.templateDataModel)
        # self.testTextEdit = QtWidgets.QTextEdit()
        # ���������� � ��������� ����������� (+�������)
        self.startTime = QtWidgets.QComboBox()
        self.endTime = QtWidgets.QComboBox()
        self.checkTimeInterval = QtWidgets.QCheckBox()
        # ������ ��� �������� ������ �������������� �������������
        self.bad_joining_comboboxModel = QtGui.QStandardItemModel()
        #
        self.select_flag = QtWidgets.QComboBox()
        # ��������
        self.chbx_for_all_bad_joining = QtWidgets.QCheckBox()
        self.chbx_for_all_joining = QtWidgets.QCheckBox()
        # ������������� ����������� ��������� ����
        self.initUI()

    # ������������� ��������� ����
    def initUI(self):
        # ������ ����
        self.initMenu()
        # ����������� ������
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget_grid_layout = QtWidgets.QGridLayout()
        central_widget.setLayout(central_widget_grid_layout)
        # ������ ������ ������������ �������
        treeview_frame = QtWidgets.QFrame()
        treeview_frame_layout = QtWidgets.QGridLayout()
        treeview_frame.setLayout(treeview_frame_layout)
        treeview_frame_layout.addWidget(self.templateDataTree)
        # treeview_frame_layout.addWidget(self.testTextEdit)
        # ������ ����� ���� � ����������, ������������ � �������
        bottom_frame = QtWidgets.QFrame()
        bottom_frame.setFixedSize(800, 80)
        bottom_frame_layout = QtWidgets.QGridLayout()
        bottom_frame.setLayout(bottom_frame_layout)
        # ��������
        self.chbx_for_all_bad_joining.setChecked(True)
        bottom_frame_layout.addWidget(QtWidgets.QLabel("��� ���� ���������."), 0, 0)
        bottom_frame_layout.addWidget(self.chbx_for_all_bad_joining, 0, 1)
        bottom_frame_layout.addWidget(QtWidgets.QLabel("��� ����"), 1, 0)
        bottom_frame_layout.addWidget(self.chbx_for_all_joining, 1, 1)
        self.chbx_for_all_bad_joining.stateChanged.connect(lambda: True if (self.chbx_for_all_bad_joining.isChecked() == False) else self.chbx_for_all_joining.setChecked(False))
        self.chbx_for_all_joining.stateChanged.connect(lambda: True if (self.chbx_for_all_joining.isChecked() == False) else self.chbx_for_all_bad_joining.setChecked(False))
        bottom_frame_layout.addItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 1, 2)        
        # ���������� � ��������� ����������� (+�������)
        self.startTime.setFixedWidth(80)
        self.endTime.setFixedWidth(80)
        # ��������� ������ ����������� ������
        self.startTime.setStyleSheet("combobox-popup: 0;")
        self.endTime.setStyleSheet("combobox-popup: 0;")
        #
        self.startTime.currentIndexChanged.connect(lambda: self.timeIntervals(startselect=1))
        #
        timeedits_frame = QtWidgets.QFrame()
        timeedits_frame.setFixedSize(200, 70)
        timeedits_layout = QtWidgets.QGridLayout()
        timeedits_frame.setLayout(timeedits_layout)
        #
        timeedits_layout.addItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 1, 0)
        timeedits_layout.addWidget(QtWidgets.QLabel("������:"), 0, 1)
        timeedits_layout.addWidget(self.startTime, 1, 1)
        timeedits_layout.addWidget(QtWidgets.QLabel("���������:"), 0, 2)
        timeedits_layout.addWidget(self.endTime, 1, 2)
        bottom_frame_layout.addWidget(timeedits_frame, 0, 3)
        self.timeIntervals()
        timeedits_layout.addWidget(self.checkTimeInterval, 1, 4)
        timeedits_layout.addItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 1, 5)
        # ��������� � �������
        self.select_flag.setMinimumWidth(100)
        self.select_flag.setMaximumWidth(100)
        self.select_flag.addItem('���� 0', 0)
        self.select_flag.addItem('���� 1', 1)
        bottom_frame_layout.addWidget(self.select_flag, 1, 4)
        # ������
        btn_set_flag = QtWidgets.QPushButton('���������')
        btn_set_flag.clicked.connect(self.btn_clk)
        bottom_frame_layout.addWidget(btn_set_flag, 1, 5)
        bottom_frame_layout.addItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 1, 6)
        # ���������� �������
        central_widget_grid_layout.addWidget(treeview_frame)
        central_widget_grid_layout.addWidget(bottom_frame)
        # ����
        self.setWindowTitle("�������� �������")
        self.setFixedSize(800, 600)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # ������������� ������ ����
    def initMenu(self):
        self.openXmlAction.triggered.connect(self.openXml)
        self.saveXmlAction.triggered.connect(self.saveXml)
        self.exitAction.triggered.connect(QtWidgets.qApp.quit)
        #
        filemenu = self.main_menu.addMenu('&����')
        filemenu.addAction(self.openXmlAction)
        filemenu.addAction(self.saveXmlAction)
        filemenu.addAction(self.exitAction)
        #
        self.saveXmlAction.setEnabled(False)
    
    # ��������� ������ ��������� ���������� (+ �������� ������������ ������ ���������� � ��������� ������ ������� � ������ ��������)
    def timeIntervals(self, check=0, startselect=0, endselect=0):
        # ���������
        def generator(one = ["00:00"]):
            self.endTime.clear()
            curtime = [int(t) for t in one[0].split(':')]
            dt = datetime.combine(date.today(), time(curtime[0], curtime[1])) + timedelta(minutes=30)
            while(dt.time().strftime("%H:%M") != "00:00"):
                one.append(dt.time().strftime("%H:%M"))
                dt += timedelta(minutes=30)
            one.append("00:00")
            if one[0] == "00:00":
                self.startTime.addItems(one)
                self.endTime.addItems(one)
            else:
                print(one[1:])
                self.endTime.addItems(one[1:])
        #
        if check == 1:
            if ((datetime.strptime(self.startTime.currentText(), "%H:%M") > datetime.strptime(self.endTime.currentText(), "%H:%M")) \
                 and (self.checkTimeInterval.isChecked() == True)):
                if (self.endTime.currentText() == "00:00"): # �������� ��� ��������� � 23:30 �� 00:00
                    return(True)
                self.message("�� ��������� ������ ������!")
                return(False)
            elif (self.checkTimeInterval.isChecked() == True):
                return(True)
        else:
            generator()
        if startselect == 1:
            generator(one = [self.startTime.currentText()])
            # if self.startTime.currentText() == "00:00":

    # ���������� ������ ������ ��� treeview
    def xmlToTreeView(self, root):
        self.bad_joining_comboboxModel.clear()
        rootItem = QtGui.QStandardItem()
        measuringpoint = QtGui.QStandardItem()
        measuringpoint_item = ""
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
                period = QtGui.QStandardItem(str(child.attrib['start']+" - "+child.attrib['end']+" --> [ "+child[0].text+" ]"))
                measuringchannel.appendRow(period)
            #
            if child.tag == 'value':
                try:
                    period.appendRow(QtGui.QStandardItem(child.text+" : "+child.attrib['status']))
                except:
                    period.appendRow(QtGui.QStandardItem(child.text))
                try:
                    child.attrib['status'] == '1'
                    measuringpoint.setBackground(QtGui.QColor("#F15A24"))
                    measuringpoint_list.append(measuringpoint_item)
                    measuringchannel.setBackground(QtGui.QColor("#F15A24"))
                    period.setBackground(QtGui.QColor("#F15A24"))
                except:
                    pass
        bad_joining_combobox = []            
        for joining in measuringpoint_list:
            if joining not in bad_joining_combobox:
                bad_joining_combobox.append(joining)
                self.bad_joining_comboboxModel.appendRow(QtGui.QStandardItem(joining))
        # ���������� ������ � ������ � �������� � treeview
        self.saveXmlAction.setEnabled(True)
        # �������� �������� �������
        self.templateDataTree.setExpanded(self.templateDataModel.index(0, 0), True)
    
    # ��������� ������ �������
    def changeStatus(self, measuringchannel, start="", end="", time_interval_flag=0):
        for period in measuringchannel:
            if period.attrib['start'] == start:
                time_interval_flag = 0
            if time_interval_flag == 0:
                for value in period:
                    if self.select_flag.currentData() == 0:
                        try:
                            del value.attrib['status']
                        except:
                            pass
                    else:
                        value.set('status', "1")
            if period.attrib['end'] == end:
                time_interval_flag = 1
        return measuringchannel

    # ��������� ������� ������� �� ������ "���������"
    def btn_clk(self):
        if self.timeIntervals(check=1):
            start = "".join(str(self.startTime.currentText()).split(":"))
            end = "".join(str(self.endTime.currentText()).split(":"))
            time_interval_flag = 1
        else:
            start = ""
            end = ""
            time_interval_flag = 0
        try:
            # ���� ���� ��������� � treeview
            selected = self.templateDataModel.itemData(self.templateDataTree.currentIndex())[0]
        except:
            selected = ''
        if self.templateDataModel.rowCount() < 1:
            self.message("��������� ��������� �����.")
        else:
            self.templateDataModel.clear()
            root = self.tree.getroot()
            # ���� ��� �������� ����� (������ ��������� �������������)
            if (self.chbx_for_all_bad_joining.isChecked() == False) and (self.chbx_for_all_joining.isChecked() == False):
                measuringpoint_flag = 0 # ���� ������ �������������, ��� ��������� ����� �� �����������
                for child in root.iterfind('.//'):
                    if (child.tag == 'measuringpoint') and (child.attrib['name'] == selected):
                        measuringpoint_flag = 1
                        for measuringchannel in child:
                            # ������� �������� �� ���������� �������
                            measuringchannel = self.changeStatus(measuringchannel, start, end, time_interval_flag)
                            # for period in measuringchannel:
                                # if period.attrib['start'] == start:
                                #     time_interval_flag = 0
                                # if time_interval_flag == 0:
                                #     for value in period:
                                #         if self.select_flag.currentData() == 0:
                                #             try:
                                #                 del value.attrib['status']
                                #             except:
                                #                 pass
                                #         else:
                                #             value.set('status', "1")
                                # if period.attrib['end'] == end:
                                #     time_interval_flag = 1
                if measuringpoint_flag == 0:
                    self.message("���������� ������� �������������!")
            # ��������� ������ � ��������������� ���������������
            if (self.chbx_for_all_bad_joining.isChecked() == True) and (self.chbx_for_all_joining.isChecked() == False):
                # ������ �� ������ �� ������ ������ �������������� �������������
                for index in range(0, self.bad_joining_comboboxModel.rowCount()):
                    for measuringpoint in root.findall("./area/measuringpoint"):
                        if measuringpoint.attrib['name'] == self.bad_joining_comboboxModel.data(self.bad_joining_comboboxModel.index(index, 0)):
                            for measuringchannel in measuringpoint:
                                # ������� �������� �� ���������� �������
                                measuringchannel = self.changeStatus(measuringchannel, start, end, time_interval_flag)
                                # for period in measuringchannel:
                                    # for value in period:
                                    #     if self.select_flag.currentData() == 0:
                                    #         try:
                                    #             del value.attrib['status']
                                    #         except:
                                    #             pass
                                    #     else:
                                    #         value.set('status', "1")
            # �������� �� ����� ������ �������������
            if (self.chbx_for_all_bad_joining.isChecked() == False) and (self.chbx_for_all_joining.isChecked() == True):
                for child in root.iterfind('.//'):
                    if (child.tag == 'measuringpoint'):
                        for measuringchannel in child:
                            # ������� �������� �� ���������� �������
                            measuringchannel = self.changeStatus(measuringchannel, start, end, time_interval_flag)
                            # for period in measuringchannel:
                                # for value in period:
                                #     if self.select_flag.currentData() == 0:
                                #         try:
                                #             del value.attrib['status']
                                #         except:
                                #             pass
                                #     else:
                                #         value.set('status', "1")
            self.xmlToTreeView(root)

    # ������� ���������� � ������ "�����" ������
    def saveHeader(self, saveFileName=""):
        if (saveFileName == ""):
            if path.exists(self.templateXMLfile):
                try:
                    with open(self.templateXMLfile, "r", encoding="windows-1251") as f:
                        for i in range(1, 4):
                            self.header.append(f.readline())
                    f.close()
                    return 0
                except Exception as e:
                    self.message("������ �������� ������: {0}".format(e))
                    return 1
        else:
            try:
                with open(saveFileName, "r+", encoding='windows-1251') as f:
                    filecache = f.readlines()
                    f.seek(0)
                    for i in range(0, 2):
                        del filecache[0]
                    filecache = self.header + filecache
                    for i in filecache:
                        start = i.find("start")
                        end = i.find("end")
                        if (start > end):
                            i = i[:end-1]+i[end-1]+i[start:][:12]+" "+i[end:][:10]+">\n"
                        f.write(i)
                f.close()
                return 0
            except Exception as e:
                self.message("������ ������ ������: {0}".format(e))
                return 1

    # ������� �������� XML-������
    def openXml(self):
        if self.templateDataModel.rowCount() > 0:
            self.message("������� �����", 1)
            self.templateDataModel.clear()
        self.templateXMLfile = ""
        self.templateXMLfile, _ = QtWidgets.QFileDialog().getOpenFileName(self, '������� �����', path.dirname(path.realpath(__file__)), '����� XML (*xml)')
        # ���������� "�����" ������ 
        if not self.saveHeader():
            if path.exists(self.templateXMLfile):
                self.tree.__init__(file=self.templateXMLfile)
                self.xmlToTreeView(self.tree.getroot())
    
    # ���������� ������ � ����
    def saveXml(self):
        savefile, _ = QtWidgets.QFileDialog.getSaveFileName(self, '��������� �����', self.templateXMLfile, '����� XML (*xml)')
        try:
            self.tree.write(savefile, encoding='windows-1251')
        except Exception as e:
            self.message("������ ������ ������: {0}".format(e))
            return 1
        self.saveHeader(savefile) 

    # ���������
    def message(self, msg, save=0):
        mb = QtWidgets.QMessageBox()
        if save == 1:
            btn = mb.question(self, "���������", msg, QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        else:
            btn = mb.question(self, "���������", msg, QtWidgets.QMessageBox.Ok)
        #   
        if btn == QtWidgets.QMessageBox.Yes:
            self.saveXml()
        else:
            pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindows()
    sys.exit(app.exec_())