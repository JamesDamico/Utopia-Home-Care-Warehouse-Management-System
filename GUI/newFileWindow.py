# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newFileWindow(object):
    def setupUi(self, newFileWindow):
        newFileWindow.setObjectName("newFileWindow")
        newFileWindow.resize(269, 323)
        self.label_3 = QtWidgets.QLabel(newFileWindow)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(newFileWindow)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 30, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(newFileWindow)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(newFileWindow)
        self.comboBox.setGeometry(QtCore.QRect(120, 70, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(newFileWindow)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(newFileWindow)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 110, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(newFileWindow)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(newFileWindow)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 150, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(newFileWindow)
        self.label_7.setGeometry(QtCore.QRect(20, 190, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(newFileWindow)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 190, 111, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_8 = QtWidgets.QLabel(newFileWindow)
        self.label_8.setGeometry(QtCore.QRect(20, 230, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(newFileWindow)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 230, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_3 = QtWidgets.QPushButton(newFileWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 280, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(newFileWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 280, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(newFileWindow)
        QtCore.QMetaObject.connectSlotsByName(newFileWindow)

    def retranslateUi(self, newFileWindow):
        _translate = QtCore.QCoreApplication.translate
        newFileWindow.setWindowTitle(_translate("newFileWindow", "Dialog"))
        self.label_3.setText(_translate("newFileWindow", "Box Number:"))
        self.label_4.setText(_translate("newFileWindow", "Type:"))
        self.comboBox.setItemText(0, _translate("newFileWindow", "Clinical"))
        self.comboBox.setItemText(1, _translate("newFileWindow", "Personnel"))
        self.comboBox.setItemText(2, _translate("newFileWindow", "Pediatric"))
        self.label_5.setText(_translate("newFileWindow", "First Name: "))
        self.label_6.setText(_translate("newFileWindow", "Last Name: "))
        self.label_7.setText(_translate("newFileWindow", "Office:"))
        self.comboBox_2.setItemText(0, _translate("newFileWindow", "Babylon"))
        self.comboBox_2.setItemText(1, _translate("newFileWindow", "Bronx"))
        self.comboBox_2.setItemText(2, _translate("newFileWindow", "Brooklyn"))
        self.comboBox_2.setItemText(3, _translate("newFileWindow", "Connecticut"))
        self.comboBox_2.setItemText(4, _translate("newFileWindow", "Florida"))
        self.comboBox_2.setItemText(5, _translate("newFileWindow", "Hempstead"))
        self.comboBox_2.setItemText(6, _translate("newFileWindow", "Kings Park Village"))
        self.comboBox_2.setItemText(7, _translate("newFileWindow", "North Carolina"))
        self.comboBox_2.setItemText(8, _translate("newFileWindow", "Patchogue"))
        self.comboBox_2.setItemText(9, _translate("newFileWindow", "Pennsylvania"))
        self.comboBox_2.setItemText(10, _translate("newFileWindow", "Queens"))
        self.comboBox_2.setItemText(11, _translate("newFileWindow", "Riverhead"))
        self.comboBox_2.setItemText(12, _translate("newFileWindow", "Rockville Centre"))
        self.comboBox_2.setItemText(13, _translate("newFileWindow", "South Carolina"))
        self.comboBox_2.setItemText(14, _translate("newFileWindow", "Westbury"))
        self.label_8.setText(_translate("newFileWindow", "Year:"))
        self.pushButton_3.setText(_translate("newFileWindow", "Add File"))
        self.pushButton_4.setText(_translate("newFileWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newFileWindow = QtWidgets.QDialog()
    ui = Ui_newFileWindow()
    ui.setupUi(newFileWindow)
    newFileWindow.show()
    sys.exit(app.exec_())
