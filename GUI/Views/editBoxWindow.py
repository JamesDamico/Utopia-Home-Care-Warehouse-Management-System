# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editBoxWindow(object):
    def setupUi(self, editBoxWindow):
        editBoxWindow.setObjectName("editBoxWindow")
        editBoxWindow.resize(244, 269)
        self.radioButton = QtWidgets.QRadioButton(editBoxWindow)
        self.radioButton.setGeometry(QtCore.QRect(30, 60, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(editBoxWindow)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 60, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(editBoxWindow)
        self.label.setGeometry(QtCore.QRect(20, 30, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.boxNumberInput = QtWidgets.QLineEdit(editBoxWindow)
        self.boxNumberInput.setGeometry(QtCore.QRect(30, 90, 113, 20))
        self.boxNumberInput.setObjectName("boxNumberInput")
        self.label_2 = QtWidgets.QLabel(editBoxWindow)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.shelfNumberInput = QtWidgets.QLineEdit(editBoxWindow)
        self.shelfNumberInput.setGeometry(QtCore.QRect(30, 170, 113, 20))
        self.shelfNumberInput.setObjectName("shelfNumberInput")
        self.saveBoxButton = QtWidgets.QPushButton(editBoxWindow)
        self.saveBoxButton.setGeometry(QtCore.QRect(80, 220, 75, 23))
        self.saveBoxButton.setObjectName("saveBoxButton")
        self.cancelButton = QtWidgets.QPushButton(editBoxWindow)
        self.cancelButton.setGeometry(QtCore.QRect(160, 220, 75, 23))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(editBoxWindow)
        QtCore.QMetaObject.connectSlotsByName(editBoxWindow)

    def retranslateUi(self, editBoxWindow):
        _translate = QtCore.QCoreApplication.translate
        editBoxWindow.setWindowTitle(_translate("editBoxWindow", "Edit Box"))
        self.radioButton.setText(_translate("editBoxWindow", "Manually"))
        self.radioButton_2.setText(_translate("editBoxWindow", "Auto Generate"))
        self.label.setText(_translate("editBoxWindow", "Box Number:"))
        self.label_2.setText(_translate("editBoxWindow", "Shelf Number:"))
        self.saveBoxButton.setText(_translate("editBoxWindow", "Save Box"))
        self.cancelButton.setText(_translate("editBoxWindow", "Cancel"))

