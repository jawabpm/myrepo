# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nodemcu.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(400, 400)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.groupBox = QtWidgets.QGroupBox(Frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 211, 111))
        self.groupBox.setObjectName("groupBox")
        self.l1 = QtWidgets.QLabel(self.groupBox)
        self.l1.setGeometry(QtCore.QRect(10, 20, 65, 15))
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(self.groupBox)
        self.l2.setGeometry(QtCore.QRect(10, 50, 65, 15))
        self.l2.setObjectName("l2")
        self.l3 = QtWidgets.QLabel(self.groupBox)
        self.l3.setGeometry(QtCore.QRect(10, 80, 65, 15))
        self.l3.setObjectName("l3")
        self.ssid = QtWidgets.QLineEdit(self.groupBox)
        self.ssid.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.ssid.setObjectName("ssid")
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setGeometry(QtCore.QRect(90, 50, 113, 20))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(90, 80, 113, 20))
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setObjectName("password")
        self.groupBox_2 = QtWidgets.QGroupBox(Frame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 381, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.uploadfile = QtWidgets.QPushButton(self.groupBox_2)
        self.uploadfile.setGeometry(QtCore.QRect(290, 20, 75, 23))
        self.uploadfile.setObjectName("uploadfile")
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(10, 230, 381, 161))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.flashstart = QtWidgets.QPushButton(Frame)
        self.flashstart.setGeometry(QtCore.QRect(130, 190, 150, 25))
        self.flashstart.setObjectName("flashstart")
        self.groupBox_3 = QtWidgets.QGroupBox(Frame)
        self.groupBox_3.setGeometry(QtCore.QRect(230, 10, 161, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.port = QtWidgets.QComboBox(self.groupBox_3)
        self.port.setGeometry(QtCore.QRect(80, 30, 73, 22))
        self.port.setObjectName("port")
        self.l4 = QtWidgets.QLabel(self.groupBox_3)
        self.l4.setGeometry(QtCore.QRect(10, 30, 31, 16))
        self.l4.setObjectName("l4")
        self.l4_2 = QtWidgets.QLabel(self.groupBox_3)
        self.l4_2.setGeometry(QtCore.QRect(10, 60, 61, 31))
        self.l4_2.setObjectName("l4_2")
        self.baud = QtWidgets.QComboBox(self.groupBox_3)
        self.baud.setGeometry(QtCore.QRect(80, 70, 73, 22))
        self.baud.setObjectName("baud")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "NodeMCU"))
        self.groupBox.setTitle(_translate("Frame", "WiFi Setup"))
        self.l1.setText(_translate("Frame", "SSID"))
        self.l2.setText(_translate("Frame", "Username"))
        self.l3.setText(_translate("Frame", "Password"))
        self.groupBox_2.setTitle(_translate("Frame", "LUA file"))
        self.uploadfile.setText(_translate("Frame", "Select Files"))
        self.flashstart.setText(_translate("Frame", "Flash"))
        self.groupBox_3.setTitle(_translate("Frame", "Communication"))
        self.l4.setText(_translate("Frame", "Port"))
        self.l4_2.setText(_translate("Frame", "Baud Rate"))
        self.baud.setItemText(0, _translate("Frame", "2400"))
        self.baud.setItemText(1, _translate("Frame", "4800"))
        self.baud.setItemText(2, _translate("Frame", "9600"))
        self.baud.setItemText(3, _translate("Frame", "14400"))
        self.baud.setItemText(4, _translate("Frame", "19200"))
        self.baud.setItemText(5, _translate("Frame", "28800"))
        self.baud.setItemText(6, _translate("Frame", "38400"))
        self.baud.setItemText(7, _translate("Frame", "56000"))
        self.baud.setItemText(8, _translate("Frame", "57600"))
        self.baud.setItemText(9, _translate("Frame", "115200"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

