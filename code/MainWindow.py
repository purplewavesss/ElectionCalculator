from PyQt5 import QtWidgets
from UiMainWindow import UiMainWindow


class MainWindow(QtWidgets.QMainWindow, UiMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_ui(self)
