from PyQt5 import QtCore, QtWidgets
from PyQt5.QtNetwork import QTcpSocket
from sim import Ui_Form
class Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.setupUi(self)
        self.tcp_socket = QTcpSocket()
        self.tcp_socket.readyRead.connect(self.on_read)
        self.pushButton.clicked.connect(self.on_switch)
        self.pushButton_send.clicked.connect(self.on_send)

    def on_switch(self):
        if self.pushButton.text() == 'connect':
            self.tcp_socket.connectToHost(self.lineEdit_ip.text(), int(self.lineEdit_port.text()))
            if not self.tcp_socket.waitForConnected(2500):
                msg = self.tcp_socket.errorString()
                QtWidgets.QMessageBox.critical(self, "Error", msg)
            else:
                self.pushButton.setText('disconnect')
        else:
            self.tcp_socket.disconnectFromHost()
            self.pushButton.setText('connect')

    def on_send(self):
        if self.tabWidget_func.currentIndex() == 0:
            self.ats_operate()
        elif self.tabWidget_func.currentIndex() == 1:
            self.opm_operate()
        else:
            self.status_operate()

    def ats_operate(self):
        out = QtCore.QByteArray()
        out.append(701, bytes(b'\x00'))
        out.append(bytes([0, 4]))

        out.append(bytes([0, 0]))
        out.append(bytes([0, self.spinBox_p1_at1.value()]))
        out.append(bytes([int(self.lineEdit_p1_dt1.text()) & 0x7F, int(self.lineEdit_p1_dt1.text()) & 0xFF]))
        out.append(bytes([0, self.spinBox_p1_at2.value()]))
        out.append(bytes([int(self.lineEdit_p1_dt2.text()) & 0x7F, int(self.lineEdit_p1_dt2.text()) & 0xFF]))
        out.append(bytes([0, self.spinBox_p1_at3.value()]))
        out.append(bytes([int(self.lineEdit_p1_dt3.text()) & 0x7F, int(self.lineEdit_p1_dt3.text()) & 0xFF]))

        out.append(bytes([0, 0]))
        out.append(bytes([0, self.spinBox_2_at1.value()]))
        out.append(bytes([int(self.lineEdit_p2_dt1.text()) & 0x7F, int(self.lineEdit_p2_dt1.text()) & 0xFF]))
        out.append(bytes([0, self.spinBox_p2_at1.value()]))
        out.append(bytes([int(self.lineEdit_p2_dt2.text()) & 0x7F, int(self.lineEdit_p2_dt2.text()) & 0xFF]))
        out.append(bytes([0, self.spinBox_p2_at1.value()]))
        out.append(bytes([int(self.lineEdit_p2_dt3.text()) & 0x7F, int(self.lineEdit_p2_dt3.text()) & 0xFF]))

        out.append(bytes([0, 0]))
        out.append(bytes([0, self.spinBox_p3_at1.value()]))
        out.append(bytes([int(self.lineEdit_p3_dt1.text()) & 0x7F, int(self.lineEdit_p3_dt1.text()) & 0xFF]))
        out.append(bytes([0, self.spinBox_p3_at1.value()]))
        out.append(bytes([int(self.lineEdit_p3_dt2.text()) & 0x7F, int(self.lineEdit_p3_dt2.text()) & 0xFF]))
        out.append(bytes([0, self.spinBox_p3_at1.value()]))
        out.append(bytes([int(self.lineEdit_p3_dt3.text()) & 0x7F, int(self.lineEdit_p3_dt3.text()) & 0xFF]))

        out.append(bytes([0, 0]))
        out.append(bytes([0, self.spinBox_p4_at1.value()]))
        out.append(bytes([int(self.lineEdit_p4_dt1.text()) & 0x7F, int(self.lineEdit_p4_dt1.text()) & 0xFF]))
        out.append(bytes([0, self.spinBox_p4_at1.value()]))
        out.append(bytes([int(self.lineEdit_p4_dt2.text()) & 0x7F, int(self.lineEdit_p4_dt2.text()) & 0xFF]))
        out.append(bytes([0, self.spinBox_p4_at1.value()]))
        out.append(bytes([int(self.lineEdit_p4_dt3.text()) & 0x7F, int(self.lineEdit_p4_dt3.text()) & 0xFF]))

        out.append(95 * 14, bytes(b'\x00'))
        out.append(68, bytes(b'\x00'))
        out.append(32, bytes(b'\x00'))
        out.append(128, bytes(b'\x00'))
        out.append(336, bytes(b'\x00'))
        out.append(16, bytes(b'\x00'))
        out.append(224, bytes(b'\x00'))

        self.tcp_socket.write(out)
    def opm_operate(self):
        if self.radioButton_limit.isChecked():
            property = '1'
        else:
            property = '0'

        property += '000000000000'
        if self.radioButton_priority.isChecked():
            property += '1'
        else:
            property += '0'
        if self.radioButton_type.isChecked():
            property += '1'
        else:
            property += '0'
        if self.radioButton_display.isChecked():
            property += '1'
        else:
            property += '0'
        property = int(property, base=2)
        out = QtCore.QByteArray()
        out.append(bytes([(property & 0xFF00) >> 8, (property & 0x00FF)]))

        time = QtCore.QDateTime.fromString(self.dateTimeEdit_start.text(), "MM/dd/yyyy HH:mm:ss")
        out.append(bytes([(time.toTime_t() & 0xFF000000) >> 24, (time.toTime_t() & 0x00FF0000) >> 16,
                          (time.toTime_t() & 0x0000FF00) >> 8, (time.toTime_t() & 0x000000FF)]))
        time = QtCore.QDateTime.fromString(self.dateTimeEdit_end.text(), "MM/dd/yyyy HH:mm:ss")
        out.append(bytes([(time.toTime_t() & 0xFF000000) >> 24, (time.toTime_t() & 0x00FF0000) >> 16,
                          (time.toTime_t() & 0x0000FF00) >> 8, (time.toTime_t() & 0x000000FF)]))
        out.append(self.textEdit.toPlainText().encode('unicode_escape'))
        if 1029 - out.size() > 0:
            out.append(1029 - out.size(), b'\x00')
        else:
            out.remove(1030, out.size() - 1029)
        out.append(40 * 2, b'\x00')
        region = '0000000000000'
        if self.comboBox_s1_dp.currentText() == 'yes':
            region += '1'
        else:
            region += '0'
        if self.comboBox_s1_up.currentText() == 'yes':
            region += '1'
        else:
            region += '0'
        if self.comboBox_s1_sh.currentText() == 'yes':
            region += '1'
        else:
            region += '0'
        region = int(region, base=2)
        out.replace(1030 + (self.spinBox_si1.value() - 1) * 2, 2, bytes([region]))
        region = ''
        if self.comboBox_s2_dp.currentText() == 'yes':
            region += '1'
        else:
            region += '0'
        if self.comboBox_s2_up.currentText() == 'yes':
            region += '1'
        else:
            region += '0'
        if self.comboBox_s2_sh.currentText() == 'yes':
            region += '1'
        else:
            region += '0'
        region = int(region, base=2)
        out.replace(1030 + (self.spinBox_si2.value() - 1) * 2, 2, bytes([region]))
        out.append(51 * 2, b'\x00')
        if int(self.lineEdit_ti1.text()) == 1:
            out.replace(1080, 2, bytes([1]))
        else:
            ti2 = int(self.lineEdit_ti2.text())
            out.replace(1080 + self.spinBox_tsn2.value() * 2, 2, bytes([(ti2 & 0xFF00) >> 8, ti2 & 0x00FF]))
            ti3 = int(self.lineEdit_ti3.text())
            out.replace(1080 + self.spinBox_tsn3.value() * 2, 2, bytes([(ti3 & 0xFF00) >> 8, ti3 & 0x00FF]))
        self.tcp_socket.write(out)

    def status_operate(self):
        out = QtCore.QByteArray()
        out.append(bytes([(self.spinBox_sn.value() & 0xFF00) >> 8, (self.spinBox_sn.value() & 0x00FF)]))
        out.append(b'\x00\x00\x00\x06\x06\x04')
        out.append(bytes([(self.spinBox_st.value() & 0xFF00) >> 8, (self.spinBox_st.value() & 0x00FF)]))
        out.append(bytes([(self.spinBox_nr.value() & 0xFF00) >> 8, (self.spinBox_nr.value() & 0x00FF)]))
        self.tcp_socket.write(out)

    def on_read(self):
        self.textEdit_recv.setText(self.tcp_socket.readAll().data().hex().upper())