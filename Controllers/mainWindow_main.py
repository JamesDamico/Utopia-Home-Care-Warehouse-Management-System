import sys
from Views.mainWindow import Ui_MainWindow
from Controllers.newFileWindow_main import NewFileWindow
from Controllers.newBoxWindow_main import NewBoxWindow
from Controllers.editFileWindow_main import EditFileWindow
from Controllers.editBoxWindow_main import EditBoxWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Model.model import *


class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.current_file_data = None
        self.current_box_data = None

        # Set Window Icon
        # self.ui.setWindowIcon(QtGui.QIcon("../Images/dbicon.png"))

        # Connect newFileButton and newBoxButton up to their respective functions
        self.ui.newFileButton.clicked.connect(self.open_new_file_window)
        self.ui.newBoxButton.clicked.connect(self.open_new_box_window)

        # Connect search button to search function
        self.ui.fileSearchButton.clicked.connect(self.file_search)
        self.ui.boxSearchButton.clicked.connect(self.box_search)

        # Load data
        self.load_data()

        # Event Filter
        self.ui.fileTable.viewport().installEventFilter(self)
        self.ui.boxTable.viewport().installEventFilter(self)


    # Capture double click event 
    def eventFilter(self, source, event):
        # File Table
        if (event.type() == QtCore.QEvent.MouseButtonDblClick and
            event.buttons() == QtCore.Qt.LeftButton and
            source is self.ui.fileTable.viewport()):
            item = self.ui.fileTable.itemAt(event.pos())
            if item is not None:
                #print('dblclick:', item.row(), item.column())
                self.open_file_edit_window(item.row())
        
        # Box Table
        if (event.type() == QtCore.QEvent.MouseButtonDblClick and
            event.buttons() == QtCore.Qt.LeftButton and
            source is self.ui.boxTable.viewport()):
            item = self.ui.boxTable.itemAt(event.pos())
            if item is not None:
                #print('dblclick:', item.row(), item.column())
                self.open_box_edit_window(item.row())

        return super(MainWindow, self).eventFilter(source, event)


    def open_file_edit_window(self, row):
        new_ui = EditFileWindow(self)
        new_ui.pass_data(self.current_file_data[row])
        new_ui.exec()


    def open_box_edit_window(self, row):
        new_ui = EditBoxWindow(self)
        new_ui.pass_data(self.current_box_data[row])
        new_ui.exec()


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
        data = select_all_from_files()
        self.load_file_table(data)

        # Load Boxes
        data = select_all_from_boxes()
        self.load_box_table(data)


    # Search for certain files in the database
    def file_search(self):
        combo_box_text = self.ui.fileSearchComboBox.currentText()
        input_text = self.ui.fileSearchInput.text()

        if combo_box_text == "All":
            data = select_all_from_files()
            self.ui.fileSearchInput.setText("")
        elif self.ui.fileSearchInput.text() == "":
            self.show_popup("Error", "Must enter search term into input box")
            return
        
        if combo_box_text == "Box #":
            try:
                data = search_query("files", "box_number", input_text)
            except:
                self.show_popup("Error", "Can only search for Box # by using a whole number.")
                self.ui.fileSearchInput.setText("")
                return
        elif combo_box_text == "Last Name":
            data = search_query("files", "last_name", input_text)
        elif combo_box_text == "Office":
            data = search_query("files", "office", input_text)
        elif combo_box_text == "Year":
            data = search_query("files", "year", input_text)

        self.load_file_table(data)


    # Search for certain files in the database
    def box_search(self):
        combo_box_text = self.ui.boxSearchComboBox.currentText()
        input_text = self.ui.boxSearchInput.text()

        if combo_box_text == "All":
            data = select_all_from_boxes()
            self.ui.boxSearchInput.setText("")
        elif self.ui.boxSearchInput.text() == "":
            self.show_popup("Error", "Must enter search term into input box")
            return
        
        if combo_box_text == "Box #":
            try:
                data = search_query("boxes", "box_number", input_text)
            except:
                self.show_popup("Error", "Can only search for Box # by using a whole number.")
                self.ui.boxSearchInput.setText("")
                return
        elif combo_box_text == "Shelf #":
            data = search_query("boxes", "shelf_number", input_text)

        self.load_box_table(data)


    # Load the file table
    def load_file_table(self, data):
        # Setting current data
        self.current_file_data = data

        self.clear_file_table()
        self.ui.fileTable.setRowCount(len(data))
        
        table_row = 0
        for row in data:
            self.ui.fileTable.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.fileTable.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.fileTable.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.fileTable.setItem(table_row, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.fileTable.setItem(table_row, 4, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.fileTable.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[6]))
            table_row += 1

    
    # Load the box table
    def load_box_table(self, data):
        # Setting current data
        self.current_box_data = data

        self.clear_box_table()
        self.ui.boxTable.setRowCount(len(data))

        table_row = 0
        for row in data:
            self.ui.boxTable.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.boxTable.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            table_row += 1


    # Clear the file table
    def clear_file_table(self):
        self.ui.fileTable.setRowCount(0)


    # Clear the box table
    def clear_box_table(self):
        self.ui.boxTable.setRowCount(0)


    # Show popup messages
    def show_popup(self, popup_type, popup_msg):
        # Setup the MessageBox
        msg = QMessageBox()

        # Title the window
        msg.setWindowTitle(f"{popup_type}")

        # Set text inside the window
        if popup_type == "Error":
            msg.setText(f"Error: {popup_msg}")
        elif popup_type == "Success":
            msg.setText(f"Success: {popup_msg}")

        # Set the icon
        if popup_type == "Error":
            msg.setIcon(QMessageBox.Warning)
        elif popup_type == "Success":
            msg.setIcon(QMessageBox.Information)

        # Add buttons to the bottom
        msg.setStandardButtons(QMessageBox.Cancel)

        x = msg.exec_()        


def show_main_window():
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())
