# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1042, 751)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.templateDataTree = QtWidgets.QTreeView(self.frame_2)
        self.templateDataTree.setObjectName("templateDataTree")
        self.verticalLayout.addWidget(self.templateDataTree)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_18 = QtWidgets.QFrame(self.centralwidget)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_20 = QtWidgets.QFrame(self.frame_18)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_17 = QtWidgets.QFrame(self.frame_20)
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_selected_measuringpoint = QtWidgets.QLabel(self.frame_17)
        self.label_selected_measuringpoint.setObjectName("label_selected_measuringpoint")
        self.verticalLayout_15.addWidget(self.label_selected_measuringpoint)
        self.comboBox_selected_measuringpoint = QtWidgets.QComboBox(self.frame_17)
        self.comboBox_selected_measuringpoint.setObjectName("comboBox_selected_measuringpoint")
        self.verticalLayout_15.addWidget(self.comboBox_selected_measuringpoint)
        self.verticalLayout_16.addWidget(self.frame_17)
        self.horizontalLayout_8.addWidget(self.frame_20)
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_4 = QtWidgets.QFrame(self.frame_19)
        self.frame_4.setEnabled(True)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.startTime_label = QtWidgets.QLabel(self.frame_4)
        self.startTime_label.setObjectName("startTime_label")
        self.verticalLayout_5.addWidget(self.startTime_label)
        self.startPeriod_comboBox = QtWidgets.QComboBox(self.frame_4)
        self.startPeriod_comboBox.setObjectName("startPeriod_comboBox")
        self.verticalLayout_5.addWidget(self.startPeriod_comboBox)
        self.horizontalLayout_11.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_19)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.endTime_label = QtWidgets.QLabel(self.frame_5)
        self.endTime_label.setObjectName("endTime_label")
        self.verticalLayout_6.addWidget(self.endTime_label)
        self.endPeriod_comboBox = QtWidgets.QComboBox(self.frame_5)
        self.endPeriod_comboBox.setObjectName("endPeriod_comboBox")
        self.verticalLayout_6.addWidget(self.endPeriod_comboBox)
        self.horizontalLayout_11.addWidget(self.frame_5)
        self.horizontalLayout_8.addWidget(self.frame_19)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.frame_18)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 200))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_7 = QtWidgets.QFrame(self.tab_1)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.measuringpointType_label = QtWidgets.QLabel(self.frame_12)
        self.measuringpointType_label.setObjectName("measuringpointType_label")
        self.verticalLayout_8.addWidget(self.measuringpointType_label)
        self.comboBox_measuringpoint_type = QtWidgets.QComboBox(self.frame_12)
        self.comboBox_measuringpoint_type.setObjectName("comboBox_measuringpoint_type")
        self.verticalLayout_8.addWidget(self.comboBox_measuringpoint_type)
        self.horizontalLayout_7.addWidget(self.frame_12)
        self.frame_10 = QtWidgets.QFrame(self.frame_11)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.selectFlag_label = QtWidgets.QLabel(self.frame_10)
        self.selectFlag_label.setObjectName("selectFlag_label")
        self.verticalLayout_7.addWidget(self.selectFlag_label)
        self.comboBox_select_flag = QtWidgets.QComboBox(self.frame_10)
        self.comboBox_select_flag.setObjectName("comboBox_select_flag")
        self.verticalLayout_7.addWidget(self.comboBox_select_flag)
        self.horizontalLayout_7.addWidget(self.frame_10)
        self.horizontalLayout_2.addWidget(self.frame_11)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame_7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_16 = QtWidgets.QFrame(self.tab_2)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_6 = QtWidgets.QFrame(self.frame_16)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_save_a_plus = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox_save_a_plus.setObjectName("checkBox_save_a_plus")
        self.verticalLayout_4.addWidget(self.checkBox_save_a_plus)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.label_a_plus = QtWidgets.QLabel(self.frame_6)
        self.label_a_plus.setObjectName("label_a_plus")
        self.verticalLayout_4.addWidget(self.label_a_plus)
        self.lineEdit_a_plus = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_a_plus.setObjectName("lineEdit_a_plus")
        self.verticalLayout_4.addWidget(self.lineEdit_a_plus)
        self.horizontalLayout_9.addWidget(self.frame_6)
        self.frame_14 = QtWidgets.QFrame(self.frame_16)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.checkBox_save_a_minus = QtWidgets.QCheckBox(self.frame_14)
        self.checkBox_save_a_minus.setObjectName("checkBox_save_a_minus")
        self.verticalLayout_9.addWidget(self.checkBox_save_a_minus)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem5)
        self.label_a_minus = QtWidgets.QLabel(self.frame_14)
        self.label_a_minus.setObjectName("label_a_minus")
        self.verticalLayout_9.addWidget(self.label_a_minus)
        self.lineEdit_a_minus = QtWidgets.QLineEdit(self.frame_14)
        self.lineEdit_a_minus.setObjectName("lineEdit_a_minus")
        self.verticalLayout_9.addWidget(self.lineEdit_a_minus)
        self.horizontalLayout_9.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_16)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.checkBox_save_r_plus = QtWidgets.QCheckBox(self.frame_15)
        self.checkBox_save_r_plus.setObjectName("checkBox_save_r_plus")
        self.verticalLayout_12.addWidget(self.checkBox_save_r_plus)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem6)
        self.label_r_plus = QtWidgets.QLabel(self.frame_15)
        self.label_r_plus.setObjectName("label_r_plus")
        self.verticalLayout_12.addWidget(self.label_r_plus)
        self.lineEdit_r_plus = QtWidgets.QLineEdit(self.frame_15)
        self.lineEdit_r_plus.setObjectName("lineEdit_r_plus")
        self.verticalLayout_12.addWidget(self.lineEdit_r_plus)
        self.horizontalLayout_9.addWidget(self.frame_15)
        self.frame_13 = QtWidgets.QFrame(self.frame_16)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.checkBox_save_r_minus = QtWidgets.QCheckBox(self.frame_13)
        self.checkBox_save_r_minus.setObjectName("checkBox_save_r_minus")
        self.verticalLayout_13.addWidget(self.checkBox_save_r_minus)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem7)
        self.label_r_minus = QtWidgets.QLabel(self.frame_13)
        self.label_r_minus.setObjectName("label_r_minus")
        self.verticalLayout_13.addWidget(self.label_r_minus)
        self.lineEdit_r_minus = QtWidgets.QLineEdit(self.frame_13)
        self.lineEdit_r_minus.setObjectName("lineEdit_r_minus")
        self.verticalLayout_13.addWidget(self.lineEdit_r_minus)
        self.horizontalLayout_9.addWidget(self.frame_13)
        self.verticalLayout_14.addWidget(self.frame_16)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_21 = QtWidgets.QFrame(self.tab_3)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_22 = QtWidgets.QFrame(self.frame_21)
        self.frame_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_A_change = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_A_change.setObjectName("pushButton_A_change")
        self.verticalLayout_10.addWidget(self.pushButton_A_change)
        self.horizontalLayout_12.addWidget(self.frame_22)
        self.frame_23 = QtWidgets.QFrame(self.frame_21)
        self.frame_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pushButton_R_change = QtWidgets.QPushButton(self.frame_23)
        self.pushButton_R_change.setObjectName("pushButton_R_change")
        self.verticalLayout_11.addWidget(self.pushButton_R_change)
        self.horizontalLayout_12.addWidget(self.frame_23)
        spacerItem8 = QtWidgets.QSpacerItem(437, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.horizontalLayout_10.addWidget(self.frame_21)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem9)
        self.pushButton_apply = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.verticalLayout_3.addWidget(self.pushButton_apply)
        self.horizontalLayout_6.addWidget(self.frame_9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.horizontalLayout_5.addWidget(self.frame_8)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1042, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_selected_measuringpoint.setText(_translate("MainWindow", "TextLabel"))
        self.startTime_label.setText(_translate("MainWindow", "TextLabel"))
        self.endTime_label.setText(_translate("MainWindow", "TextLabel"))
        self.measuringpointType_label.setText(_translate("MainWindow", "TextLabel"))
        self.selectFlag_label.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Tab 1"))
        self.checkBox_save_a_plus.setText(_translate("MainWindow", "CheckBox"))
        self.label_a_plus.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox_save_a_minus.setText(_translate("MainWindow", "CheckBox"))
        self.label_a_minus.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox_save_r_plus.setText(_translate("MainWindow", "CheckBox"))
        self.label_r_plus.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox_save_r_minus.setText(_translate("MainWindow", "CheckBox"))
        self.label_r_minus.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.pushButton_A_change.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_R_change.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 3"))
        self.pushButton_apply.setText(_translate("MainWindow", "PushButton"))
