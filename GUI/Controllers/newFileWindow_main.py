import sys
from PyQt5.QtWidgets import *
from GUI.Views.newFileWindow import Ui_newFileWindow
from model import *

class NewFileWindow(QDialog):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_newFileWindow()
        self.ui.setupUi(self)

        # Connect addFileButton to add_file()
        self.ui.addFileButton.clicked.connect(lambda: self.add_file())


    def add_file(self):
        if self.ui.boxNumberInput.text() == "":
            msg = "Box Number can't be empty"
            self.show_popup(msg)
            return
        elif self.ui.firstNameInput.text() == "":
            msg = "First Name can't be empty"
            self.show_popup(msg)
            return
        elif self.ui.lastNameInput.text() == "":
            msg = "Last Name can't be empty"
            self.show_popup(msg)
            return
        elif self.ui.yearInput.text() == "":
            msg = "Year can't be empty"
            self.show_popup(msg)
            return
        try:
            form_data = (int(self.ui.boxNumberInput.text()), str(self.ui.typeComboBox.currentText()), 
                        str(self.ui.firstNameInput.text()), str(self.ui.lastNameInput.text()),
                        str(self.ui.officeComboBox.currentText()), str(self.ui.yearInput.text()))
            add_new_file(form_data)
        except ValueError:
            msg = "Box Number must be a whole number"
            self.show_popup(msg)
        else:
            print("Good job")
            self.close()


    def show_popup(self, error):
        # Setup the MessageBox
        msg = QMessageBox()

        # Title the window
        msg.setWindowTitle("Error")

        # Set text inside the window
        msg.setText(f"Error: {error}")

        # Set the icon
        msg.setIcon(QMessageBox.Warning)

        # Add buttons to the bottom
        msg.setStandardButtons(QMessageBox.Cancel)

        x = msg.exec_()

