# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newBoxWindow(object):
    def setupUi(self, newBoxWindow):
        newBoxWindow.setObjectName("newBoxWindow")
        newBoxWindow.resize(244, 269)
        self.radioButton = QtWidgets.QRadioButton(newBoxWindow)
        self.radioButton.setGeometry(QtCore.QRect(30, 60, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(newBoxWindow)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 60, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(newBoxWindow)
        self.label.setGeometry(QtCore.QRect(20, 30, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(newBoxWindow)
        self.lineEdit.setGeometry(QtCore.QRect(30, 90, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(newBoxWindow)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(newBoxWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 170, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(newBoxWindow)
        self.pushButton.setGeometry(QtCore.QRect(80, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(newBoxWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 220, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(newBoxWindow)
        QtCore.QMetaObject.connectSlotsByName(newBoxWindow)

    def retranslateUi(self, newBoxWindow):
        _translate = QtCore.QCoreApplication.translate
        newBoxWindow.setWindowTitle(_translate("newBoxWindow", "Dialog"))
        self.radioButton.setText(_translate("newBoxWindow", "Manually"))
        self.radioButton_2.setText(_translate("newBoxWindow", "Auto Generate"))
        self.label.setText(_translate("newBoxWindow", "Box Number:"))
        self.label_2.setText(_translate("newBoxWindow", "Shelf Number:"))
        self.pushButton.setText(_translate("newBoxWindow", "Add Box"))
        self.pushButton_2.setText(_translate("newBoxWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newBoxWindow = QtWidgets.QDialog()
    ui = Ui_newBoxWindow()
    ui.setupUi(newBoxWindow)
    newBoxWindow.show()
    sys.exit(app.exec_())
