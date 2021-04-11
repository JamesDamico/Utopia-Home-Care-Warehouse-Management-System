import sys
from PyQt5.QtWidgets import *
from Views.newBoxWindow import Ui_newBoxWindow
from Model.model import *

class NewBoxWindow(QDialog):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_newBoxWindow()
        self.ui.setupUi(self)

        # Connect addBoxButton to add_box()
        self.ui.addBoxButton.clicked.connect(lambda: self.add_box())

        # Connect cancelButton to close function
        self.ui.cancelButton.clicked.connect(lambda: self.close())

        # Connect Radio Buttons
        self.ui.manualRadioButton.toggled.connect(lambda: self.toggle_line_edit(False))
        self.ui.autoGenRadioButton.toggled.connect(lambda: self.toggle_line_edit(True))


    # Add a box to the database
    def add_box(self):
        """
        Adds a box to the database.
        """
        # Check to see if user selected a radio button
        if not self.ui.manualRadioButton.isChecked() and not self.ui.autoGenRadioButton.isChecked():
            self.show_popup("Error", "Must select Manual or Auto Generate")
            return

        # Check to see if box number input is empty
        if self.ui.boxNumberInput.text() == "" and not self.ui.autoGenRadioButton.isChecked():
            self.show_popup("Error", "Box Number can't be empty")
            return

        if not self.ui.autoGenRadioButton.isChecked():
            try:
                exists = box_number_exists(self.ui.boxNumberInput.text())
            except:
                self.show_popup("Error", "Box Number must be a whole number")
                return

            # Check if the box number exists
            if exists:
                msg = f"Box {self.ui.boxNumberInput.text()} already exists. Enter a different box number."
                self.show_popup("Error", msg)
                return 
        
        # Try and add to database
        if self.ui.autoGenRadioButton.isChecked():
            try:
                form_data = (self.ui.shelfNumberInput.text(), )
                added_id = add_new_box("auto", form_data)             
            except ValueError:
                self.show_popup("Error", "Box Number must be a whole number")
            else:
                self.close()
                self.show_popup("Success", f"You have added Box {added_id}")
        else:
            try:
                form_data = (self.ui.boxNumberInput.text(), self.ui.shelfNumberInput.text())
                add_new_box("manual", form_data)             
            except ValueError:
                self.show_popup("Error", "Box Number must be a whole number")
            else:
                self.close()
                self.show_popup("Success", f"You have added Box {form_data[0]}")
        self.parent().load_data()


    # Toggles the line edit
    def toggle_line_edit(self, toggle_state):
        """
        Will toggle the line edit between active and inactive based on what 
        radio button is selected.
        
        Takes in toggle_state as a boolean.
        """
        # If True disable, if False enable
        self.ui.boxNumberInput.setDisabled(toggle_state)

        # When disabling the line edit, clear it as well
        if toggle_state == True:
            self.ui.boxNumberInput.clear()


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