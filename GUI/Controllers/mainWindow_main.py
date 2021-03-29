import sys
from GUI.Views.mainWindow import Ui_MainWindow
from GUI.Controllers.newFileWindow_main import NewFileWindow
from GUI.Controllers.newBoxWindow_main import NewBoxWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from model import *


class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect newFileButton and newBoxButton up to their respective functions
        self.ui.newFileButton.clicked.connect(self.open_new_file_window)
        self.ui.newBoxButton.clicked.connect(self.open_new_box_window)

        # Connect search button to search function
        self.ui.fileSearchButton.clicked.connect(self.search)

        # Load data on load
        self.load_data()


    # Open newFileWindow
    def open_new_file_window(self): 
        new_ui = NewFileWindow(self)
        new_ui.exec()


    # Open newBoxWindow
    def open_new_box_window(self):
        new_ui = NewBoxWindow(self)
        new_ui.exec()


    # Load data into tables on load
    def load_data(self):
        # Load Files
        files = select_all_from_files()
        self.ui.fileTable.setRowCount(len(files))
        
        table_row = 0
        for row in files:
            self.ui.fileTable.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.fileTable.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.fileTable.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.fileTable.setItem(table_row, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.fileTable.setItem(table_row, 4, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.fileTable.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[6]))
            table_row += 1

        # Load Boxes
        boxes = select_all_from_boxes()
        self.ui.boxTable.setRowCount(len(boxes))

        table_row = 0
        for row in boxes:
            self.ui.boxTable.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.boxTable.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            table_row += 1

    def search(self):
        pass


def show_main_window():
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())

def reload_tables():
    print("Testing")