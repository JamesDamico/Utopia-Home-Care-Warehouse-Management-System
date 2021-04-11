import sys
from PyQt5.QtWidgets import *
from Views.editBoxWindow import Ui_editBoxWindow
from Model.model import *

class EditBoxWindow(QDialog):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_editBoxWindow()
        self.ui.setupUi(self)

        # Data that is sent into this window
        self.data = None

        # Connect saveBoxButton to add_file()
        self.ui.saveBoxButton.clicked.connect(lambda: self.save_box())

        # Connect cancelButton to close function
        self.ui.cancelButton.clicked.connect(lambda: self.close())

        # Connect deleteButton to close delete_box()
        self.ui.deleteButton.clicked.connect(lambda: self.delete_box())

        # Make boxNumberInput read only
        self.ui.boxNumberInput.setDisabled(True)


    # Save a box
    def save_box(self):
        """
        Save changes made to the current box's data.
        """
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
        """
        Delete a box from the database.
        """

        # Confirm user want to delete box
        delete = self.delete_box_confirmation(self.data[0])

        # Ask if user want to delete all files inside 
        delete_files = self.delete_all_files_confirmation()

        # If user wants to delete the box and all files inside:
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
        # User just wants to delete the box and leave the files
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
        """
        Prompts the user to confirm if they want to delete the box from the database.

        Takes in box_num as a parameter to let the user know what box they're deleting. 
        """
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
        """
        Prompts the user to ask if they want to delete all the files inside the box.
        """
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


    # Used by other classes to pass data to this popup
    def pass_data(self, data):
        """
        Takes in data as a parameter and sets self.data to whatever was passed in.
        """
        self.data = data
        self.load_input_fields()


    # Load data into input fields
    def load_input_fields(self):
        """
        Loads data into the input fields when dialog is displayed on screen.
        """
        self.ui.boxNumberInput.setText(str(self.data[0]))
        self.ui.shelfNumberInput.setText(self.data[1])


