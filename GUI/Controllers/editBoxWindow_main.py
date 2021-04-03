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


    def save_box(self):
        pass


    def pass_data(self, data):
        self.data = data
        self.load_input_fields(data)


    def load_input_fields(self, data):
        self.ui.boxNumberInput.setText(str(data[0]))
        self.ui.shelfNumberInput.setText(data[1])


