import sys
from PyQt5.QtWidgets import *
from GUI.Views.editBoxWindow import Ui_editBoxWindow
from model import *

class EditBoxWindow(QDialog):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_editBoxWindow()
        self.ui.setupUi(self)

        self.data = None

        # Connect saveBoxButton to add_file()
        self.ui.saveBoxButton.clicked.connect(lambda: self.save_box())

        # Connect cancelButton to close function
        self.ui.cancelButton.clicked.connect(lambda: self.close())

        # Connect deleteButton to close delete_box()
        self.ui.deleteButton.clicked.connect(lambda: self.delete_box())

        # Make boxNumberInput read only
        self.ui.boxNumberInput.setDisabled(True)


    # Save changes to a box
    def save_box(self):

        try:
            form_data = (self.ui.shelfNumberInput.text(), self.ui.boxNumberInput.text())
            update_box(form_data)            
        except ValueError:
            self.show_popup("Error", "Box Number must be a whole number")
        else:
            self.close()
            self.show_popup("Success", f"You have made changes to Box {form_data[1]}")
        self.parent().load_data()
        

    # Delete a box
    def delete_box(self):
        # Confirm user want to delete box
        delete = self.delete_box_confirmation(self.data[0])

        # Ask if user want to delete all files inside 
        delete_files = self.delete_all_files_confirmation()

        if delete_box and delete_files:
            try:
                # Delete all files
                delete_all_files(self.data[0])
                # Delete box
                delete_box(self.data[0])
            except:
                self.show_popup("Error", "Problem deleting box.")
            else:
                self.show_popup("Success", f"You have deleted Box {self.data[0]} and all files inside.")
        elif delete_box:
            try:
                # Delete box
                delete_box(int(self.data[0]))
                set_box_number_null(int(self.data[0]))
            except:
                self.show_popup("Error", "Problem deleting box.")
            else:
                self.show_popup("Success", f"You have deleted Box {self.data[0]}.")

        self.close()
        self.parent().load_data()


    # Confirm you want to delete the box
    def delete_box_confirmation(self, box_num):
        msg = f"Are you sure you want to delete Box {box_num}? This action cannot be undone."

        reply = QMessageBox.question(self, "Delete Box",
                                     msg, QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            return True
        else:
            return False


    # Ask if the user wants to delete all the files in the box
    def delete_all_files_confirmation(self):
        msg = f"Would you like to delete all files inside the box?"

        reply = QMessageBox.question(self, "Delete Files",
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


    # Used by other classes to pass data to this popup
    def pass_data(self, data):
        self.data = data
        self.load_input_fields(data)


    # Load data into input fields
    def load_input_fields(self, data):
        self.ui.boxNumberInput.setText(str(data[0]))
        self.ui.shelfNumberInput.setText(data[1])


