from PyQt5 import QtWidgets
from UiSettingsDialog import UiSettingsDialog
from Settings import Settings


class SettingsDialog(UiSettingsDialog, QtWidgets.QDialog):
    def __init__(self, _settings):
        super(SettingsDialog, self).__init__()
        self.setup_ui(self)
        self.settings: Settings = _settings
