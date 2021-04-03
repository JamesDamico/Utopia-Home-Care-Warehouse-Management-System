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


    def save_file(self):
        pass


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


