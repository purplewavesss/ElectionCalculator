import sys
from PyQt5 import QtWidgets
from MainWindow import MainWindow
from gen_message_box import gen_message_box


def implement_triggers(window: MainWindow):
    window.open_action.triggered.connect(not_implemented)
    window.save_action.triggered.connect(not_implemented)
    window.exit_action.triggered.connect(exit_action_triggers)
    window.about_action.triggered.connect(about_action_triggers)
    window.settings_action.triggered.connect(not_implemented)


def exit_action_triggers():
    sys.exit()


def about_action_triggers():
    gen_message_box("About", "Created by Gavin J. Grotegut\nPre-Alpha Version\nCoded in Python\nDesigned in Qt, a GUI "
                             "framework for C++ and Python", QtWidgets.QMessageBox.Icon.Information)


def not_implemented():
    raise NotImplementedError
