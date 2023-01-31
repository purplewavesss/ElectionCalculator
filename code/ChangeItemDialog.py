from PyQt5 import QtWidgets
from UiChangeItemDialog import UiChangeItemDialog
from gen_message_box import gen_message_box


class ChangeItemDialog(QtWidgets.QDialog, UiChangeItemDialog):
    def __init__(self, _item: QtWidgets.QTableWidgetItem, _is_decimal: bool):
        super(ChangeItemDialog, self).__init__()
        self.setup_ui(self)
        self.item = _item
        self.is_decimal = _is_decimal
        self.content_line_edit.setText(self.item.text())
        self.button_box.accepted.connect(self.change_item)
        self.button_box.rejected.connect(self.reject)

    def change_item(self):
        if self.is_decimal:
            if self.content_line_edit.text().isdecimal():
                self.item.setText(self.content_line_edit.text())
                self.accept()
            else:
                gen_message_box("Invalid input!", "Votes and electorates must be integers.",
                                QtWidgets.QMessageBox.Icon.Warning)
        else:
            self.item.setText(self.content_line_edit.text())
            self.accept()
