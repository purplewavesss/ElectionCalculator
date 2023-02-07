from PyQt5 import QtWidgets
from UiSettingsDialog import UiSettingsDialog
from Settings import Settings
from gen_message_box import gen_message_box


class SettingsDialog(UiSettingsDialog, QtWidgets.QDialog):
    def __init__(self, _settings):
        super(SettingsDialog, self).__init__()
        self.setup_ui(self)
        self.settings: Settings = _settings
        self.implement_triggers()
        if self.settings.votes_forced:
            self.vote_number.setText(str(self.settings.forced_vote_num))

    def implement_triggers(self):
        self.highest_average_box.toggled.connect(self.ham_trigger)
        self.largest_remainder_box.toggled.connect(self.lrm_trigger)
        self.button_box.accepted.connect(self.change_settings)
        self.button_box.rejected.connect(self.reject)
        self.vote_number.textEdited.connect(lambda: self.button_box.button(
                                            QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(True))

    def ham_trigger(self):
        self.largest_remainder_box.setChecked(not self.highest_average_box.isChecked())
        self.button_box.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(True)

    def lrm_trigger(self):
        self.highest_average_box.setChecked(not self.largest_remainder_box.isChecked())
        self.button_box.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(True)

    def change_settings(self):
        for group_box in [self.election_method_box, self.highest_average_box]:
            for radio_button in group_box.children():
                radio_button: QtWidgets.QRadioButton
                if radio_button.isChecked():
                    self.settings.current_methods[group_box.objectName()] = radio_button.objectName()
        self.settings.method_type = self.highest_average_box.isChecked()

        if self.vote_number.text().isdecimal() and self.vote_number.text() != "" and self.vote_number.text() != "0":
            self.settings.votes_forced = True
            self.settings.forced_vote_num = int(self.vote_number.text())
            self.accept()

        elif not self.vote_number.text().isdecimal() and self.vote_number.text() != "":
            gen_message_box("Invalid number of votes!", "Number of votes must be an integer.",
                            QtWidgets.QMessageBox.Icon.Warning)

        else:
            self.settings.votes_forced = False
            self.accept()
