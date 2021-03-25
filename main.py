from PyQt5 import QtWidgets
from GUI.mainWindow import Ui_MainWindow

def show_main_window():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    show_main_window()



