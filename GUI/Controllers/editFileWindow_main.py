import sys
from PyQt5.QtWidgets import *
from GUI.Views.editFileWindow import Ui_editFileWindow
from model import *

class EditFileWindow(QDialog):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_editFileWindow()
        self.ui.setupUi(self)

        self.data = None

        # Connect addFileButton to add_file()
        self.ui.saveFileButton.clicked.connect(lambda: self.save_file())

        # Connect cancelButton to close function
        self.ui.cancelButton.clicked.connect(lambda: self.close())
        
        # Connect deleteButton to delete_file()
        self.ui.deleteButton.clicked.connect(lambda: self.delete_file())

    def save_file(self):
        # Check if any fields are empty
        if self.ui.boxNumberInput.text() == "NULL":
            msg = "Must assign a box number to this file"
            self.show_popup("Error", msg)
            return
        elif self.ui.boxNumberInput.text() == "":
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

        try:
            form_data = (self.ui.boxNumberInput.text(),
                self.ui.typeComboBox.currentText(),
                self.ui.lastNameInput.text(),
                self.ui.firstNameInput.text(),
                self.ui.officeComboBox.currentText(),
                self.ui.yearInput.text(), self.data[0])
            update_file(form_data)
        except ValueError:
            self.show_popup("Error", "Box Number must be a whole number")
        else:
            self.close()
            self.show_popup("Success", f"You have saved changes to {form_data[3]} {form_data[2]}")
        
        self.parent().load_data()

    
    # Delete a file
    def delete_file(self):
        # Confirm user wants to delete file
        delete = self.delete_file_confirmation()

        if delete:
            try:
                delete_file(self.data[0])
            except:
                self.show_popup("Error", "Problem deleting file.")
            else:
                self.show_popup("Success", f"You have deleted {self.data[4]} {self.data[3]}'s file.")

        self.close()
        self.parent().load_data()

    # Confirm you want to delete the box
    def delete_file_confirmation(self):
        msg = f"Are you sure you want to delete {self.data[4]} {self.data[3]}'s file? This action cannot be undone."

        reply = QMessageBox.question(self, "Delete Box",
                                     msg, QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            return True
        else:
            return False


    # Error/Info Popups   
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


    def pass_data(self, data):
        self.data = data
        self.load_input_fields(data)


    def load_input_fields(self, data):
        self.ui.boxNumberInput.setText(str(self.data[1]))
        self.ui.typeComboBox.setCurrentText(self.data[2])
        self.ui.firstNameInput.setText(self.data[3])
        self.ui.lastNameInput.setText(self.data[4])
        self.ui.officeComboBox.setCurrentText(self.data[5])
        self.ui.yearInput.setText(self.data[6])


