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
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 111))
        self.groupBox.setObjectName("groupBox")
        self.l1 = QtWidgets.QLabel(self.groupBox)
        self.l1.setGeometry(QtCore.QRect(60, 20, 47, 13))
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(self.groupBox)
        self.l2.setGeometry(QtCore.QRect(60, 50, 47, 13))
        self.l2.setObjectName("l2")
        self.l3 = QtWidgets.QLabel(self.groupBox)
        self.l3.setGeometry(QtCore.QRect(60, 80, 47, 13))
        self.l3.setObjectName("l3")
        self.ssid = QtWidgets.QLineEdit(self.groupBox)
        self.ssid.setGeometry(QtCore.QRect(140, 20, 113, 20))
        self.ssid.setObjectName("ssid")
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setGeometry(QtCore.QRect(140, 50, 113, 20))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(140, 80, 113, 20))
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
        self.textEdit.setObjectName("textEdit")
        self.flashstart = QtWidgets.QPushButton(Frame)
        self.flashstart.setGeometry(QtCore.QRect(130, 190, 150, 25))
        self.flashstart.setObjectName("flashstart")

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

