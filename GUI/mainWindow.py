# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UHC.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.newFileWindow import Ui_newFileWindow
from GUI.newBoxWindow import Ui_newBoxWindow

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1054, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boxTable = QtWidgets.QTableWidget(self.centralwidget)
        self.boxTable.setGeometry(QtCore.QRect(50, 150, 321, 351))
        self.boxTable.setObjectName("boxTable")
        self.boxTable.setColumnCount(3)
        self.boxTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.boxTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.boxTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.boxTable.setHorizontalHeaderItem(2, item)
        self.fileTable = QtWidgets.QTableWidget(self.centralwidget)
        self.fileTable.setGeometry(QtCore.QRect(400, 150, 611, 351))
        self.fileTable.setObjectName("fileTable")
        self.fileTable.setColumnCount(6)
        self.fileTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(5, item)
        self.newBoxButton = QtWidgets.QPushButton(self.centralwidget)
        self.newBoxButton.setGeometry(QtCore.QRect(290, 510, 81, 31))
        self.newBoxButton.setObjectName("newBoxButton")
        self.newFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.newFileButton.setGeometry(QtCore.QRect(930, 510, 81, 31))
        self.newFileButton.setObjectName("newFileButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(510, 110, 501, 41))
        self.groupBox.setObjectName("groupBox")
        self.fileSearchComboBox = QtWidgets.QComboBox(self.groupBox)
        self.fileSearchComboBox.setGeometry(QtCore.QRect(80, 10, 141, 21))
        self.fileSearchComboBox.setObjectName("fileSearchComboBox")
        self.fileSearchComboBox.addItem("")
        self.fileSearchComboBox.addItem("")
        self.fileSearchComboBox.addItem("")
        self.fileSearchComboBox.addItem("")
        self.fileSearchInput = QtWidgets.QLineEdit(self.groupBox)
        self.fileSearchInput.setGeometry(QtCore.QRect(240, 10, 131, 21))
        self.fileSearchInput.setObjectName("fileSearchInput")
        self.fileSearchButton = QtWidgets.QPushButton(self.groupBox)
        self.fileSearchButton.setGeometry(QtCore.QRect(390, 10, 71, 23))
        self.fileSearchButton.setObjectName("fileSearchButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 110, 321, 41))
        self.groupBox_2.setObjectName("groupBox_2")
        self.boxSearchInput = QtWidgets.QLineEdit(self.groupBox_2)
        self.boxSearchInput.setGeometry(QtCore.QRect(160, 10, 71, 21))
        self.boxSearchInput.setObjectName("boxSearchInput")
        self.boxSearchButton = QtWidgets.QPushButton(self.groupBox_2)
        self.boxSearchButton.setGeometry(QtCore.QRect(240, 10, 75, 23))
        self.boxSearchButton.setObjectName("boxSearchButton")
        self.fileSearchComboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.fileSearchComboBox_2.setGeometry(QtCore.QRect(70, 10, 81, 21))
        self.fileSearchComboBox_2.setObjectName("fileSearchComboBox_2")
        self.fileSearchComboBox_2.addItem("")
        self.fileSearchComboBox_2.addItem("")
        self.fileSearchComboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1054, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Hook newFileButton and newBoxButton up to their respective functions
        self.newFileButton.clicked.connect(self.open_new_file_window)
        self.newBoxButton.clicked.connect(self.open_new_box_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.boxTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Box #"))
        item = self.boxTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Shelf #"))
        item = self.boxTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "File Count"))
        item = self.fileTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Box #"))
        item = self.fileTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.fileTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.fileTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.fileTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Office"))
        item = self.fileTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Year"))
        self.newBoxButton.setText(_translate("MainWindow", "New Box"))
        self.newFileButton.setText(_translate("MainWindow", "New File"))
        self.groupBox.setTitle(_translate("MainWindow", "File Search"))
        self.fileSearchComboBox.setItemText(0, _translate("MainWindow", "Box #"))
        self.fileSearchComboBox.setItemText(1, _translate("MainWindow", "Last Name"))
        self.fileSearchComboBox.setItemText(2, _translate("MainWindow", "Office"))
        self.fileSearchComboBox.setItemText(3, _translate("MainWindow", "Year"))
        self.fileSearchButton.setText(_translate("MainWindow", "Search"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Box Search"))
        self.boxSearchButton.setText(_translate("MainWindow", "Search"))
        self.fileSearchComboBox_2.setItemText(0, _translate("MainWindow", "Box #"))
        self.fileSearchComboBox_2.setItemText(1, _translate("MainWindow", "Shelf #"))
        self.fileSearchComboBox_2.setItemText(2, _translate("MainWindow", "File Count"))

    # Open newFileWindow
    def open_new_file_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_newFileWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    # Open newBoxWindow
    def open_new_box_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_newBoxWindow()
        self.ui.setupUi(self.window)
        self.window.show()
