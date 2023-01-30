from PyQt5 import QtWidgets


def gen_message_box(title: str, message: str, icon: QtWidgets.QMessageBox.Icon):
    message_box = QtWidgets.QMessageBox()
    message_box.setWindowTitle(title)
    message_box.setIcon(icon)
    message_box.setText(message)
    message_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
    message_box.exec()
