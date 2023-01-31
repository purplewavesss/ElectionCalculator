import re
from PyQt5 import QtWidgets, QtCore, QtGui
from Columns import Columns
from ChangeItemDialog import ChangeItemDialog
from gen_message_box import gen_message_box


class ElectionTable(QtWidgets.QTableWidget):
    def __init__(self, parent: QtWidgets.QWidget, geometry: QtCore.QRect, rows: int, columns: int, can_edit: bool):
        super(ElectionTable, self).__init__()
        self.setParent(parent)
        self.setGeometry(geometry)
        self.edit_dict: dict[tuple[int, int], bool] = {}

        # Set rows and columns
        self.setRowCount(rows)
        self.setColumnCount(columns)
        self.initialize_rows()
        self.generate_edit_dict()

        # Set edit triggers
        if not can_edit:
            self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.itemClicked.connect(self.item_clicked)

        # Set font
        font = QtGui.QFont()
        font.setPointSize(8)
        self.setFont(font)

        # Set header properties
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setDefaultSectionSize(80)
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(35)

    def initialize_rows(self):
        for x in range(self.rowCount()):
            item = QtWidgets.QTableWidgetItem()
            self.setVerticalHeaderItem(x, item)

        for x in range(self.columnCount()):
            item = QtWidgets.QTableWidgetItem()
            self.setHorizontalHeaderItem(x, item)
            for y in range(self.rowCount()):
                item = QtWidgets.QTableWidgetItem()
                self.setItem(y, x, item)

    def append_row(self, table_row: QtWidgets.QTableWidget):
        for x in range(table_row.columnCount()):
            table_row.item(0, x).setText(re.sub(",", "", table_row.item(0, x).text()))
        if str(table_row.item(0, 1).text()).isdecimal() and str(table_row.item(0, 2).text()).isdecimal():
            row_position = self.rowCount()
            self.insertRow(row_position)
            for x in range(table_row.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                self.setItem(row_position, x, item)
                self.item(row_position, x).setText(table_row.item(0, x).text())
                if x <= Columns.ELECTORATE.value:
                    self.edit_dict.update({(row_position, x): True})
                else:
                    self.edit_dict.update({(row_position, x): False})
        else:
            gen_message_box("Invalid input!", "Votes and electorates must be integers.",
                            QtWidgets.QMessageBox.Icon.Warning)

    def delete_row(self):
        if self.rowCount() > 1:
            deleted_row: int = self.rowCount()
            self.removeRow(self.rowCount() - 1)
            for x in range(self.columnCount()):
                self.edit_dict.pop((deleted_row, x))

    def generate_edit_dict(self):
        for x in range(self.rowCount()):
            for y in range(self.columnCount()):
                if y <= Columns.ELECTORATE.value:
                    self.edit_dict.update({(x, y): True})
                else:
                    self.edit_dict.update({(x, y): False})

    def clear_table(self):
        for x in range(self.rowCount() - 1):
            self.delete_row()

    @staticmethod
    def item_clicked(item: QtWidgets.QTableWidgetItem):
        if item.column() <= Columns.ELECTORATE.value and item.row() > 0:
            if item.column() > Columns.PARTY.value:
                change_item_dialog = ChangeItemDialog(item, True)
            else:
                change_item_dialog = ChangeItemDialog(item, False)
            change_item_dialog.exec()
