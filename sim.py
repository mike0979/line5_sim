# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sim.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 545)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget_func = QtWidgets.QTabWidget(Form)
        self.tabWidget_func.setObjectName("tabWidget_func")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_44 = QtWidgets.QLabel(self.tab)
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_25.addWidget(self.label_44)
        self.spinBox_p1_at1 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_p1_at1.setMaximum(255)
        self.spinBox_p1_at1.setObjectName("spinBox_p1_at1")
        self.horizontalLayout_25.addWidget(self.spinBox_p1_at1)
        self.label_45 = QtWidgets.QLabel(self.tab)
        self.label_45.setObjectName("label_45")
        self.horizontalLayout_25.addWidget(self.label_45)
        self.lineEdit_p1_dt1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_p1_dt1.setObjectName("lineEdit_p1_dt1")
        self.horizontalLayout_25.addWidget(self.lineEdit_p1_dt1)
        self.verticalLayout.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_40 = QtWidgets.QLabel(self.tab)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_23.addWidget(self.label_40)
        self.spinBox_p1_at2 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_p1_at2.setMaximum(255)
        self.spinBox_p1_at2.setObjectName("spinBox_p1_at2")
        self.horizontalLayout_23.addWidget(self.spinBox_p1_at2)
        self.label_41 = QtWidgets.QLabel(self.tab)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_23.addWidget(self.label_41)
        self.lineEdit_p1_dt2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_p1_dt2.setObjectName("lineEdit_p1_dt2")
        self.horizontalLayout_23.addWidget(self.lineEdit_p1_dt2)
        self.verticalLayout.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_42 = QtWidgets.QLabel(self.tab)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_24.addWidget(self.label_42)
        self.spinBox_p1_at3 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_p1_at3.setMaximum(255)
        self.spinBox_p1_at3.setObjectName("spinBox_p1_at3")
        self.horizontalLayout_24.addWidget(self.spinBox_p1_at3)
        self.label_43 = QtWidgets.QLabel(self.tab)
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_24.addWidget(self.label_43)
        self.lineEdit_p1_dt3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_p1_dt3.setObjectName("lineEdit_p1_dt3")
        self.horizontalLayout_24.addWidget(self.lineEdit_p1_dt3)
        self.verticalLayout.addLayout(self.horizontalLayout_24)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.spinBox_p2_at1 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_p2_at1.setMaximum(255)
        self.spinBox_p2_at1.setObjectName("spinBox_p2_at1")
        self.horizontalLayout_5.addWidget(self.spinBox_p2_at1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.lineEdit_p2_dt1 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_p2_dt1.setObjectName("lineEdit_p2_dt1")
        self.horizontalLayout_5.addWidget(self.lineEdit_p2_dt1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.spinBox_p2_at2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_p2_at2.setMaximum(255)
        self.spinBox_p2_at2.setObjectName("spinBox_p2_at2")
        self.horizontalLayout_7.addWidget(self.spinBox_p2_at2)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.lineEdit_p2_dt2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_p2_dt2.setObjectName("lineEdit_p2_dt2")
        self.horizontalLayout_7.addWidget(self.lineEdit_p2_dt2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.spinBox_p2_at3 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_p2_at3.setMaximum(255)
        self.spinBox_p2_at3.setObjectName("spinBox_p2_at3")
        self.horizontalLayout_6.addWidget(self.spinBox_p2_at3)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.lineEdit_p2_dt3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_p2_dt3.setObjectName("lineEdit_p2_dt3")
        self.horizontalLayout_6.addWidget(self.lineEdit_p2_dt3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15)
        self.spinBox_p3_at1 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_p3_at1.setMaximum(255)
        self.spinBox_p3_at1.setObjectName("spinBox_p3_at1")
        self.horizontalLayout_8.addWidget(self.spinBox_p3_at1)
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_8.addWidget(self.label_16)
        self.lineEdit_p3_dt1 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_p3_dt1.setObjectName("lineEdit_p3_dt1")
        self.horizontalLayout_8.addWidget(self.lineEdit_p3_dt1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_10.addWidget(self.label_19)
        self.spinBox_p3_at2 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_p3_at2.setMaximum(255)
        self.spinBox_p3_at2.setObjectName("spinBox_p3_at2")
        self.horizontalLayout_10.addWidget(self.spinBox_p3_at2)
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_10.addWidget(self.label_20)
        self.lineEdit_p3_dt2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_p3_dt2.setObjectName("lineEdit_p3_dt2")
        self.horizontalLayout_10.addWidget(self.lineEdit_p3_dt2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_9.addWidget(self.label_17)
        self.spinBox_p3_at3 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_p3_at3.setMaximum(255)
        self.spinBox_p3_at3.setObjectName("spinBox_p3_at3")
        self.horizontalLayout_9.addWidget(self.spinBox_p3_at3)
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_9.addWidget(self.label_18)
        self.lineEdit_p3_dt3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_p3_dt3.setObjectName("lineEdit_p3_dt3")
        self.horizontalLayout_9.addWidget(self.lineEdit_p3_dt3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_21 = QtWidgets.QLabel(self.tab_4)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_11.addWidget(self.label_21)
        self.spinBox_p4_at1 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_p4_at1.setMaximum(255)
        self.spinBox_p4_at1.setObjectName("spinBox_p4_at1")
        self.horizontalLayout_11.addWidget(self.spinBox_p4_at1)
        self.label_22 = QtWidgets.QLabel(self.tab_4)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_11.addWidget(self.label_22)
        self.lineEdit_p4_dt1 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_p4_dt1.setObjectName("lineEdit_p4_dt1")
        self.horizontalLayout_11.addWidget(self.lineEdit_p4_dt1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_25 = QtWidgets.QLabel(self.tab_4)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_13.addWidget(self.label_25)
        self.spinBox_p4_at2 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_p4_at2.setMaximum(255)
        self.spinBox_p4_at2.setObjectName("spinBox_p4_at2")
        self.horizontalLayout_13.addWidget(self.spinBox_p4_at2)
        self.label_26 = QtWidgets.QLabel(self.tab_4)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_13.addWidget(self.label_26)
        self.lineEdit_p4_dt2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_p4_dt2.setObjectName("lineEdit_p4_dt2")
        self.horizontalLayout_13.addWidget(self.lineEdit_p4_dt2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_23 = QtWidgets.QLabel(self.tab_4)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_12.addWidget(self.label_23)
        self.spinBox_p4_at3 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_p4_at3.setMaximum(255)
        self.spinBox_p4_at3.setObjectName("spinBox_p4_at3")
        self.horizontalLayout_12.addWidget(self.spinBox_p4_at3)
        self.label_24 = QtWidgets.QLabel(self.tab_4)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_12.addWidget(self.label_24)
        self.lineEdit_p4_dt3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_p4_dt3.setObjectName("lineEdit_p4_dt3")
        self.horizontalLayout_12.addWidget(self.lineEdit_p4_dt3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.tabWidget_func.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_32 = QtWidgets.QLabel(self.tab_6)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_12.addWidget(self.label_32)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.radioButton_display = QtWidgets.QRadioButton(self.tab_6)
        self.radioButton_display.setChecked(True)
        self.radioButton_display.setObjectName("radioButton_display")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_display)
        self.horizontalLayout_16.addWidget(self.radioButton_display)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_6)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.horizontalLayout_16.addWidget(self.radioButton_2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_16)
        self.label_34 = QtWidgets.QLabel(self.tab_6)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_12.addWidget(self.label_34)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.radioButton_type = QtWidgets.QRadioButton(self.tab_6)
        self.radioButton_type.setChecked(True)
        self.radioButton_type.setObjectName("radioButton_type")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_type)
        self.horizontalLayout_17.addWidget(self.radioButton_type)
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_6)
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup_2.addButton(self.radioButton_4)
        self.horizontalLayout_17.addWidget(self.radioButton_4)
        self.verticalLayout_12.addLayout(self.horizontalLayout_17)
        self.label_35 = QtWidgets.QLabel(self.tab_6)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_12.addWidget(self.label_35)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.radioButton_priority = QtWidgets.QRadioButton(self.tab_6)
        self.radioButton_priority.setChecked(True)
        self.radioButton_priority.setObjectName("radioButton_priority")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_priority)
        self.horizontalLayout_18.addWidget(self.radioButton_priority)
        self.radioButton_6 = QtWidgets.QRadioButton(self.tab_6)
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup_3.addButton(self.radioButton_6)
        self.horizontalLayout_18.addWidget(self.radioButton_6)
        self.verticalLayout_12.addLayout(self.horizontalLayout_18)
        self.label_36 = QtWidgets.QLabel(self.tab_6)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_12.addWidget(self.label_36)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.radioButton_limit = QtWidgets.QRadioButton(self.tab_6)
        self.radioButton_limit.setChecked(True)
        self.radioButton_limit.setObjectName("radioButton_limit")
        self.buttonGroup_4 = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.radioButton_limit)
        self.horizontalLayout_19.addWidget(self.radioButton_limit)
        self.radioButton_8 = QtWidgets.QRadioButton(self.tab_6)
        self.radioButton_8.setObjectName("radioButton_8")
        self.buttonGroup_4.addButton(self.radioButton_8)
        self.horizontalLayout_19.addWidget(self.radioButton_8)
        self.verticalLayout_12.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_38 = QtWidgets.QLabel(self.tab_6)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_21.addWidget(self.label_38)
        self.dateTimeEdit_start = QtWidgets.QDateTimeEdit(self.tab_6)
        self.dateTimeEdit_start.setCalendarPopup(True)
        self.dateTimeEdit_start.setObjectName("dateTimeEdit_start")
        self.horizontalLayout_21.addWidget(self.dateTimeEdit_start)
        self.verticalLayout_12.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_39 = QtWidgets.QLabel(self.tab_6)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_20.addWidget(self.label_39)
        self.dateTimeEdit_end = QtWidgets.QDateTimeEdit(self.tab_6)
        self.dateTimeEdit_end.setCalendarPopup(True)
        self.dateTimeEdit_end.setObjectName("dateTimeEdit_end")
        self.horizontalLayout_20.addWidget(self.dateTimeEdit_end)
        self.verticalLayout_12.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_37 = QtWidgets.QLabel(self.tab_6)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_22.addWidget(self.label_37)
        self.textEdit = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_22.addWidget(self.textEdit)
        self.verticalLayout_12.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_27 = QtWidgets.QLabel(self.tab_6)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_9.addWidget(self.label_27)
        self.spinBox_si1 = QtWidgets.QSpinBox(self.tab_6)
        self.spinBox_si1.setMinimum(1)
        self.spinBox_si1.setMaximum(34)
        self.spinBox_si1.setObjectName("spinBox_si1")
        self.verticalLayout_9.addWidget(self.spinBox_si1)
        self.spinBox_si2 = QtWidgets.QSpinBox(self.tab_6)
        self.spinBox_si2.setMinimum(1)
        self.spinBox_si2.setMaximum(34)
        self.spinBox_si2.setObjectName("spinBox_si2")
        self.verticalLayout_9.addWidget(self.spinBox_si2)
        self.horizontalLayout_14.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_28 = QtWidgets.QLabel(self.tab_6)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_8.addWidget(self.label_28)
        self.comboBox_s1_dp = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_s1_dp.setObjectName("comboBox_s1_dp")
        self.comboBox_s1_dp.addItem("")
        self.comboBox_s1_dp.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox_s1_dp)
        self.comboBox_s2_dp = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_s2_dp.setObjectName("comboBox_s2_dp")
        self.comboBox_s2_dp.addItem("")
        self.comboBox_s2_dp.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox_s2_dp)
        self.horizontalLayout_14.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_29 = QtWidgets.QLabel(self.tab_6)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_7.addWidget(self.label_29)
        self.comboBox_s1_up = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_s1_up.setObjectName("comboBox_s1_up")
        self.comboBox_s1_up.addItem("")
        self.comboBox_s1_up.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_s1_up)
        self.comboBox_s2_up = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_s2_up.setObjectName("comboBox_s2_up")
        self.comboBox_s2_up.addItem("")
        self.comboBox_s2_up.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_s2_up)
        self.horizontalLayout_14.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_30 = QtWidgets.QLabel(self.tab_6)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_6.addWidget(self.label_30)
        self.comboBox_s1_sh = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_s1_sh.setObjectName("comboBox_s1_sh")
        self.comboBox_s1_sh.addItem("")
        self.comboBox_s1_sh.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox_s1_sh)
        self.comboBox_s2_sh = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_s2_sh.setObjectName("comboBox_s2_sh")
        self.comboBox_s2_sh.addItem("")
        self.comboBox_s2_sh.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox_s2_sh)
        self.horizontalLayout_14.addLayout(self.verticalLayout_6)
        self.verticalLayout_12.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_31 = QtWidgets.QLabel(self.tab_6)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_10.addWidget(self.label_31)
        self.spinBox_tsn1 = QtWidgets.QSpinBox(self.tab_6)
        self.spinBox_tsn1.setEnabled(False)
        self.spinBox_tsn1.setObjectName("spinBox_tsn1")
        self.verticalLayout_10.addWidget(self.spinBox_tsn1)
        self.spinBox_tsn2 = QtWidgets.QSpinBox(self.tab_6)
        self.spinBox_tsn2.setMinimum(1)
        self.spinBox_tsn2.setMaximum(51)
        self.spinBox_tsn2.setObjectName("spinBox_tsn2")
        self.verticalLayout_10.addWidget(self.spinBox_tsn2)
        self.spinBox_tsn3 = QtWidgets.QSpinBox(self.tab_6)
        self.spinBox_tsn3.setMinimum(1)
        self.spinBox_tsn3.setMaximum(51)
        self.spinBox_tsn3.setObjectName("spinBox_tsn3")
        self.verticalLayout_10.addWidget(self.spinBox_tsn3)
        self.horizontalLayout_15.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_33 = QtWidgets.QLabel(self.tab_6)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_11.addWidget(self.label_33)
        self.lineEdit_ti1 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_ti1.setObjectName("lineEdit_ti1")
        self.verticalLayout_11.addWidget(self.lineEdit_ti1)
        self.lineEdit_ti2 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_ti2.setObjectName("lineEdit_ti2")
        self.verticalLayout_11.addWidget(self.lineEdit_ti2)
        self.lineEdit_ti3 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_ti3.setObjectName("lineEdit_ti3")
        self.verticalLayout_11.addWidget(self.lineEdit_ti3)
        self.horizontalLayout_15.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addLayout(self.horizontalLayout_15)
        self.tabWidget_func.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.tab_7)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox_sn = QtWidgets.QSpinBox(self.tab_7)
        self.spinBox_sn.setMaximum(65535)
        self.spinBox_sn.setObjectName("spinBox_sn")
        self.horizontalLayout.addWidget(self.spinBox_sn)
        self.verticalLayout_13.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab_7)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.spinBox_st = QtWidgets.QSpinBox(self.tab_7)
        self.spinBox_st.setObjectName("spinBox_st")
        self.horizontalLayout_3.addWidget(self.spinBox_st)
        self.verticalLayout_13.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.tab_7)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.spinBox_nr = QtWidgets.QSpinBox(self.tab_7)
        self.spinBox_nr.setObjectName("spinBox_nr")
        self.horizontalLayout_4.addWidget(self.spinBox_nr)
        self.verticalLayout_13.addLayout(self.horizontalLayout_4)
        self.textEdit_recv = QtWidgets.QTextEdit(self.tab_7)
        self.textEdit_recv.setReadOnly(True)
        self.textEdit_recv.setObjectName("textEdit_recv")
        self.verticalLayout_13.addWidget(self.textEdit_recv)
        self.tabWidget_func.addTab(self.tab_7, "")
        self.gridLayout.addWidget(self.tabWidget_func, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_ip = QtWidgets.QLineEdit(Form)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.horizontalLayout_2.addWidget(self.lineEdit_ip)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_port = QtWidgets.QLineEdit(Form)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.horizontalLayout_2.addWidget(self.lineEdit_port)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_send = QtWidgets.QPushButton(Form)
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout_2.addWidget(self.pushButton_send)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget_func.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "line5_sim"))
        self.label_44.setText(_translate("Form", "first train arrival time:"))
        self.label_45.setText(_translate("Form", "The destination of the first train:"))
        self.lineEdit_p1_dt1.setText(_translate("Form", "0"))
        self.label_40.setText(_translate("Form", "second train arrival time:"))
        self.label_41.setText(_translate("Form", "The destination of the second train:"))
        self.lineEdit_p1_dt2.setText(_translate("Form", "0"))
        self.label_42.setText(_translate("Form", "third train arrival time:"))
        self.label_43.setText(_translate("Form", "The destination of the third train:"))
        self.lineEdit_p1_dt3.setText(_translate("Form", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "platform_1"))
        self.label_9.setText(_translate("Form", "first train arrival time:"))
        self.label_10.setText(_translate("Form", "The destination of the first train:"))
        self.lineEdit_p2_dt1.setText(_translate("Form", "0"))
        self.label_13.setText(_translate("Form", "second train arrival time:"))
        self.label_14.setText(_translate("Form", "The destination of the second train:"))
        self.lineEdit_p2_dt2.setText(_translate("Form", "0"))
        self.label_11.setText(_translate("Form", "third train arrival time:"))
        self.label_12.setText(_translate("Form", "The destination of the third train:"))
        self.lineEdit_p2_dt3.setText(_translate("Form", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "platform_2"))
        self.label_15.setText(_translate("Form", "first train arrival time:"))
        self.label_16.setText(_translate("Form", "The destination of the first train:"))
        self.lineEdit_p3_dt1.setText(_translate("Form", "0"))
        self.label_19.setText(_translate("Form", "second train arrival time:"))
        self.label_20.setText(_translate("Form", "The destination of the second train:"))
        self.lineEdit_p3_dt2.setText(_translate("Form", "0"))
        self.label_17.setText(_translate("Form", "third train arrival time:"))
        self.label_18.setText(_translate("Form", "The destination of the third train:"))
        self.lineEdit_p3_dt3.setText(_translate("Form", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "platform_3"))
        self.label_21.setText(_translate("Form", "first train arrival time:"))
        self.label_22.setText(_translate("Form", "The destination of the first train:"))
        self.lineEdit_p4_dt1.setText(_translate("Form", "0"))
        self.label_25.setText(_translate("Form", "second train arrival time:"))
        self.label_26.setText(_translate("Form", "The destination of the second train:"))
        self.lineEdit_p4_dt2.setText(_translate("Form", "0"))
        self.label_23.setText(_translate("Form", "third train arrival time:"))
        self.label_24.setText(_translate("Form", "The destination of the third train:"))
        self.lineEdit_p4_dt3.setText(_translate("Form", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "platform_4"))
        self.tabWidget_func.setTabText(self.tabWidget_func.indexOf(self.tab_5), _translate("Form", "ats"))
        self.label_32.setText(_translate("Form", "start or stop display"))
        self.radioButton_display.setText(_translate("Form", "start"))
        self.radioButton_2.setText(_translate("Form", "stop"))
        self.label_34.setText(_translate("Form", "display type"))
        self.radioButton_type.setText(_translate("Form", "scroll"))
        self.radioButton_4.setText(_translate("Form", "full screen"))
        self.label_35.setText(_translate("Form", "priority"))
        self.radioButton_priority.setText(_translate("Form", "normal"))
        self.radioButton_6.setText(_translate("Form", "high"))
        self.label_36.setText(_translate("Form", "whether to enable time limit for playing text"))
        self.radioButton_limit.setText(_translate("Form", "disable"))
        self.radioButton_8.setText(_translate("Form", "enable"))
        self.label_38.setText(_translate("Form", "start time"))
        self.dateTimeEdit_start.setDisplayFormat(_translate("Form", "MM/dd/yyyy HH:mm:ss"))
        self.label_39.setText(_translate("Form", "end time"))
        self.dateTimeEdit_end.setDisplayFormat(_translate("Form", "MM/dd/yyyy HH:mm:ss"))
        self.label_37.setText(_translate("Form", "text content"))
        self.label_27.setText(_translate("Form", "station id"))
        self.label_28.setText(_translate("Form", "downward platform"))
        self.comboBox_s1_dp.setItemText(0, _translate("Form", "no"))
        self.comboBox_s1_dp.setItemText(1, _translate("Form", "yes"))
        self.comboBox_s2_dp.setItemText(0, _translate("Form", "no"))
        self.comboBox_s2_dp.setItemText(1, _translate("Form", "yes"))
        self.label_29.setText(_translate("Form", "upward platform"))
        self.comboBox_s1_up.setItemText(0, _translate("Form", "no"))
        self.comboBox_s1_up.setItemText(1, _translate("Form", "yes"))
        self.comboBox_s2_up.setItemText(0, _translate("Form", "no"))
        self.comboBox_s2_up.setItemText(1, _translate("Form", "yes"))
        self.label_30.setText(_translate("Form", "sation hall"))
        self.comboBox_s1_sh.setItemText(0, _translate("Form", "no"))
        self.comboBox_s1_sh.setItemText(1, _translate("Form", "yes"))
        self.comboBox_s2_sh.setItemText(0, _translate("Form", "no"))
        self.comboBox_s2_sh.setItemText(1, _translate("Form", "yes"))
        self.label_31.setText(_translate("Form", "train serial number"))
        self.label_33.setText(_translate("Form", "train id"))
        self.lineEdit_ti1.setText(_translate("Form", "0"))
        self.lineEdit_ti2.setText(_translate("Form", "0"))
        self.lineEdit_ti3.setText(_translate("Form", "0"))
        self.tabWidget_func.setTabText(self.tabWidget_func.indexOf(self.tab_6), _translate("Form", "opm"))
        self.label_3.setText(_translate("Form", "serial number:"))
        self.label_4.setText(_translate("Form", "register start position"))
        self.label_5.setText(_translate("Form", "number of registers"))
        self.tabWidget_func.setTabText(self.tabWidget_func.indexOf(self.tab_7), _translate("Form", "device status"))
        self.label.setText(_translate("Form", "ip:"))
        self.label_2.setText(_translate("Form", "port:"))
        self.pushButton.setText(_translate("Form", "connect"))
        self.pushButton_send.setText(_translate("Form", "send"))
