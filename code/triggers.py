import sys
from PyQt5 import QtWidgets
from MainWindow import MainWindow
from SettingsDialog import SettingsDialog
from Settings import Settings
from gen_message_box import gen_message_box


def implement_triggers(window: MainWindow, settings: Settings):
    window.open_action.triggered.connect(not_implemented)
    window.save_action.triggered.connect(not_implemented)
    window.exit_action.triggered.connect(exit_action_triggers)
    window.about_action.triggered.connect(about_action_triggers)
    window.settings_action.triggered.connect(lambda: settings_triggers(settings))


def exit_action_triggers():
    sys.exit()


def about_action_triggers():
    gen_message_box("About", "Created by Gavin J. Grotegut\nPre-Alpha Version\nCoded in Python\nDesigned in Qt, a GUI "
                             "framework for C++ and Python", QtWidgets.QMessageBox.Icon.Information)


def settings_triggers(settings: Settings):
    settings_dialog = SettingsDialog(settings)
    settings_dialog.exec()


def not_implemented():
    raise NotImplementedError
