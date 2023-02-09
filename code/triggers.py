import os
import sys
from PyQt5 import QtWidgets
from MainWindow import MainWindow
from SettingsDialog import SettingsDialog
from Settings import Settings
from gen_message_box import gen_message_box


def implement_triggers(window: MainWindow, settings: Settings):
    window.open_action.triggered.connect(lambda: open_action_triggers(window))
    window.save_action.triggered.connect(lambda: save_action_triggers(window))
    window.exit_action.triggered.connect(exit_action_triggers)
    window.about_action.triggered.connect(about_action_triggers)
    window.settings_action.triggered.connect(lambda: settings_triggers(settings))


def open_action_triggers(main_window: MainWindow):
    file_dialog = QtWidgets.QFileDialog()
    file_name: str = file_dialog.getOpenFileName(file_dialog, "Open Election JSON", os.path.expanduser('~') +
                                                 "/Documents", "JSON files (*.json)")[0]
    if file_name != "":
        main_window.read_json(file_name)


def save_action_triggers(main_window: MainWindow):
    main_window.has_saved = main_window.save_json()


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
