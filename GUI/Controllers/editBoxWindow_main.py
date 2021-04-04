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

        # Connect addFileButton to add_file()
        self.ui.saveBoxButton.clicked.connect(lambda: self.save_box())

        # Connect cancelButton to close function
        self.ui.cancelButton.clicked.connect(lambda: self.close())

        # Make boxNumberInput read only
        self.ui.boxNumberInput.setDisabled(True)


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
        self.ui.boxNumberInput.setText(str(data[0]))
        self.ui.shelfNumberInput.setText(data[1])


