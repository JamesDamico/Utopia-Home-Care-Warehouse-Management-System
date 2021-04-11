import sys
from PyQt5.QtWidgets import *
from Views.newFileWindow import Ui_newFileWindow
from Model.model import *

class NewFileWindow(QDialog):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_newFileWindow()
        self.ui.setupUi(self)

        # Connect addFileButton to add_file()
        self.ui.addFileButton.clicked.connect(lambda: self.add_file())

        # Connect cancelButton to close function
        self.ui.cancelButton.clicked.connect(lambda: self.close())

    
    # Add a file to the database
    def add_file(self):
        """
        Adds a file to the database.
        """
        # Check if any fields are empty
        if self.ui.boxNumberInput.text() == "":
            msg = "Box Number can't be empty"
            self.show_popup("Error", msg)
            return
        elif self.ui.firstNameInput.text() == "":
            msg = "First Name can't be empty"
            self.show_popup("Error", msg)
            return
        elif self.ui.lastNameInput.text() == "":
            msg = "Last Name can't be empty"
            self.show_popup("Error", msg)
            return
        elif self.ui.yearInput.text() == "":
            msg = "Year can't be empty"
            self.show_popup("Error", msg)
            return

        try:
            exists = box_number_exists(self.ui.boxNumberInput.text())
        except:
            self.show_popup("Error", "Box Number must be a whole number")
            return

        # Check if the box number exists
        if not exists:
            msg = f"Box {self.ui.boxNumberInput.text()} does not exist. Either enter a different box number or create a new box."
            self.show_popup("Error", msg)
            return

        # Try to add the file to the database
        try:
            form_data = (int(self.ui.boxNumberInput.text()), str(self.ui.typeComboBox.currentText()), 
                        str(self.ui.firstNameInput.text()), str(self.ui.lastNameInput.text()),
                        str(self.ui.officeComboBox.currentText()), str(self.ui.yearInput.text()))
            add_new_file(form_data)
        except ValueError:
            self.show_popup("Error", "Box Number must be a whole number")
        else:
            self.close()
            self.show_popup("Success", f"You have added {form_data[2]} {form_data[3]} to Box {form_data[0]}")
        self.parent().load_data()


    # Error/Info Popups
    def show_popup(self, popup_type, popup_msg):
        """
        Display a popup with either an error or success message.

        This function takes a popup_type which is either Error or Succes, and a popup_msg to be displayed.
        """
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