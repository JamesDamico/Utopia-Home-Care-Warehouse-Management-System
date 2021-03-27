import sys
from PyQt5.QtWidgets import *
from GUI.Views.newBoxWindow import Ui_newBoxWindow

class NewBoxWindow(QDialog):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_newBoxWindow()
        self.ui.setupUi(self)
