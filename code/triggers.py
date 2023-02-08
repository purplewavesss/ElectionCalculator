import os
import sys
import json_functions
from PyQt5 import QtWidgets
from MainWindow import MainWindow
from SettingsDialog import SettingsDialog
from Settings import Settings
from ElectionTable import ElectionTable
from SeatAllocation import SeatAllocation
from gen_message_box import gen_message_box


def implement_triggers(window: MainWindow, settings: Settings):
    window.open_action.triggered.connect(lambda: open_action_triggers(window.election_table, settings,
                                                                      window.seat_allocation))
    window.save_action.triggered.connect(not_implemented)
    window.exit_action.triggered.connect(exit_action_triggers)
    window.about_action.triggered.connect(about_action_triggers)
    window.settings_action.triggered.connect(lambda: settings_triggers(settings))


def open_action_triggers(election_table: ElectionTable, settings: Settings, seat_allocation: SeatAllocation):
    file_dialog = QtWidgets.QFileDialog()
    file_name: str = file_dialog.getOpenFileName(file_dialog, "Open Election JSON", os.path.expanduser('~') +
                                                 "/Documents", "JSON files (*.json)")[0]
    json_functions.json_parse(file_name, election_table, settings, seat_allocation)


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
