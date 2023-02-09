from PyQt5.QtWidgets import QMessageBox


def gen_message_box(title: str, message: str, icon: QMessageBox.Icon, return_msg_box: bool = False):
    message_box = QMessageBox()
    message_box.setWindowTitle(title)
    message_box.setIcon(icon)
    message_box.setText(message)
    if return_msg_box:
        return message_box
    else:
        message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        message_box.exec()
