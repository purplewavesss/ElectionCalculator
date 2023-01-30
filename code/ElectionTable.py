import re
from PyQt5 import QtWidgets, QtCore, QtGui
from gen_message_box import gen_message_box


class ElectionTable(QtWidgets.QTableWidget):
    def __init__(self, parent: QtWidgets.QWidget, geometry: QtCore.QRect, rows: int, columns: int, can_edit: bool):
        super(ElectionTable, self).__init__()
        self.setParent(parent)
        self.setGeometry(geometry)

        # Set rows and columns
        self.setRowCount(rows)
        self.setColumnCount(columns)
        self.initialize_rows()
        if not can_edit:
            self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

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
        else:
            gen_message_box("Invalid input!", "Votes and electorates must be integers.",
                            QtWidgets.QMessageBox.Icon.Warning)

    def delete_row(self):
        if self.rowCount() > 1:
            self.removeRow(self.rowCount() - 1)

    def clear_table(self):
        for x in range(self.rowCount() - 1):
            self.delete_row()
