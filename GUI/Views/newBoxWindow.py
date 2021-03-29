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
        self.manualRadioButton = QtWidgets.QRadioButton(newBoxWindow)
        self.manualRadioButton.setGeometry(QtCore.QRect(30, 60, 82, 17))
        self.manualRadioButton.setObjectName("manualRadioButton")
        self.autoGenRadioButton = QtWidgets.QRadioButton(newBoxWindow)
        self.autoGenRadioButton.setGeometry(QtCore.QRect(130, 60, 82, 17))
        self.autoGenRadioButton.setObjectName("autoGenRadioButton")
        self.label = QtWidgets.QLabel(newBoxWindow)
        self.label.setGeometry(QtCore.QRect(20, 30, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.boxNumberInput = QtWidgets.QLineEdit(newBoxWindow)
        self.boxNumberInput.setGeometry(QtCore.QRect(30, 90, 113, 20))
        self.boxNumberInput.setObjectName("boxNumberInput")
        self.label_2 = QtWidgets.QLabel(newBoxWindow)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.shelfNumberInput = QtWidgets.QLineEdit(newBoxWindow)
        self.shelfNumberInput.setGeometry(QtCore.QRect(30, 170, 113, 20))
        self.shelfNumberInput.setObjectName("shelfNumberInput")
        self.addBoxButton = QtWidgets.QPushButton(newBoxWindow)
        self.addBoxButton.setGeometry(QtCore.QRect(80, 220, 75, 23))
        self.addBoxButton.setObjectName("addBoxButton")
        self.cancelButton = QtWidgets.QPushButton(newBoxWindow)
        self.cancelButton.setGeometry(QtCore.QRect(160, 220, 75, 23))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(newBoxWindow)
        QtCore.QMetaObject.connectSlotsByName(newBoxWindow)

    def retranslateUi(self, newBoxWindow):
        _translate = QtCore.QCoreApplication.translate
        newBoxWindow.setWindowTitle(_translate("newBoxWindow", "Dialog"))
        self.manualRadioButton.setText(_translate("newBoxWindow", "Manual"))
        self.autoGenRadioButton.setText(_translate("newBoxWindow", "Auto Generate"))
        self.label.setText(_translate("newBoxWindow", "Box Number:"))
        self.label_2.setText(_translate("newBoxWindow", "Shelf Number:"))
        self.addBoxButton.setText(_translate("newBoxWindow", "Add Box"))
        self.cancelButton.setText(_translate("newBoxWindow", "Cancel"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     newBoxWindow = QtWidgets.QDialog()
#     ui = Ui_newBoxWindow()
#     ui.setupUi(newBoxWindow)
#     newBoxWindow.show()
#     sys.exit(app.exec_())
