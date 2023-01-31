# Form implementation generated from reading ui file 'changeitem.ui'
from PyQt5 import QtCore, QtWidgets


class UiChangeItemDialog(object):
    def setup_ui(self, change_item_dialog):
        change_item_dialog.setObjectName("change_item_dialog")
        change_item_dialog.resize(290, 80)
        self.button_box = QtWidgets.QDialogButtonBox(change_item_dialog)
        self.button_box.setGeometry(QtCore.QRect(45, 40, 200, 30))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label = QtWidgets.QLabel(change_item_dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 55, 20))
        self.label.setObjectName("label")
        self.content_line_edit = QtWidgets.QLineEdit(change_item_dialog)
        self.content_line_edit.setGeometry(QtCore.QRect(70, 10, 210, 20))
        self.content_line_edit.setObjectName("content_line_edit")

        self.retranslate_ui(change_item_dialog)
        QtCore.QMetaObject.connectSlotsByName(change_item_dialog)

    def retranslate_ui(self, change_item_dialog):
        _translate = QtCore.QCoreApplication.translate
        change_item_dialog.setWindowTitle(_translate("change_item_dialog", "Change Item"))
        self.label.setText(_translate("change_item_dialog", "Content:"))
