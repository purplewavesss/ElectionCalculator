import re
from PyQt5 import QtWidgets, QtCore, QtGui
from Columns import Columns
from ChangeItemDialog import ChangeItemDialog
from SeatAllocation import SeatAllocation
from gen_message_box import gen_message_box


class ElectionTable(QtWidgets.QTableWidget):
    def __init__(self, parent: QtWidgets.QWidget, geometry: QtCore.QRect, rows: int, columns: int, can_edit: bool,
                 _seat_allocation: SeatAllocation):
        super(ElectionTable, self).__init__(parent)
        self.setGeometry(geometry)
        self.edit_dict: dict[tuple[int, int], bool] = {}
        self.seat_allocation: SeatAllocation = _seat_allocation
        self.table_electorates: int = 0

        # Set rows and columns
        self.setRowCount(rows)
        self.setColumnCount(columns)
        self.initialize_rows()
        self.generate_edit_dict()

        # Set edit triggers
        if not can_edit:
            self.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
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
        """Fills a table with blank items"""
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
        """Adds a one-row table to an election table"""
        # Remove commas from input
        for x in range(table_row.columnCount()):
            table_row.item(0, x).setText(re.sub(",", "", table_row.item(0, x).text()))

        # Zero out empty values
        if (table_row.item(0, Columns.ELECTORATE.value).text() or table_row.item(0, Columns.TOTAL.value).text()) \
                == "":
            table_row.item(0, Columns.ELECTORATE.value).setText("0")

        # Check if input is valid for row added
        if str(table_row.item(0, Columns.VOTES.value).text()).isdecimal() and \
                str(table_row.item(0, Columns.ELECTORATE.value).text()).isdecimal():
            row_position = self.rowCount()

            # Insert and fill row
            self.insertRow(row_position)
            for x in range(table_row.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                self.setItem(row_position, x, item)
                self.item(row_position, x).setText(table_row.item(0, x).text())

                # Check if items are editable
                if x <= Columns.ELECTORATE.value:
                    self.edit_dict.update({(row_position, x): True})
                else:
                    self.edit_dict.update({(row_position, x): False})

            # Add to table_electorates
            self.table_electorates += int(table_row.item(0, Columns.ELECTORATE.value).text())
            self.electorate_increase()

        else:
            gen_message_box("Invalid input!", "Votes and electorates must be integers.",
                            QtWidgets.QMessageBox.Icon.Warning)

    def delete_row(self):
        if self.rowCount() > 1:
            deleted_row: int = self.rowCount() - 1
            self.table_electorates -= int(self.item(deleted_row, Columns.ELECTORATE.value).text())
            self.removeRow(deleted_row)
            for x in range(self.columnCount()):
                if x <= Columns.ELECTORATE.value:
                    self.edit_dict.pop((deleted_row, x))

    def generate_edit_dict(self):
        """Generates a dictionary determining whether items are editable"""
        for x in range(self.rowCount()):
            for y in range(self.columnCount()):
                if y <= Columns.ELECTORATE.value:
                    self.edit_dict.update({(x, y): True})
                else:
                    self.edit_dict.update({(x, y): False})

    def clear_table(self):
        """Deletes every table row except for the headers"""
        for x in range(self.rowCount() - 1):
            self.delete_row()

    def generate_party_dict(self) -> dict[str, dict[str, int]]:
        """Generates dictionary containing party info"""
        party_dict: dict[str, dict[str, int]] = {}
        for x in range(self.rowCount()):
            if x != 0:
                # Creates a dict of {party_name: {votes, electorates}}
                party_dict.update({self.item(x, Columns.PARTY.value).text(): {"votes":
                                  int(self.item(x, Columns.VOTES.value).text()), "electorates":
                                  int(self.item(x, Columns.ELECTORATE.value).text())}})
        return party_dict

    def set_value(self, rows: int, columns: int, text: str):
        item = QtWidgets.QTableWidgetItem()
        item.setText(text)
        self.setItem(rows, columns, item)

    def item_clicked(self, item: QtWidgets.QTableWidgetItem):
        if (item.column(), item.row()) in self.edit_dict:
            if item.column() > Columns.PARTY.value:
                change_item_dialog = ChangeItemDialog(item, True)
            else:
                change_item_dialog = ChangeItemDialog(item, False)
            change_item_dialog.exec()

    def electorate_increase(self):
        try:
            if self.table_electorates > self.seat_allocation.get_electorates():
                self.seat_allocation.set_electorates(self.table_electorates)
                self.seat_allocation.seat_value_changed()
        except ValueError:
            self.seat_allocation.set_electorates(self.table_electorates)
            self.seat_allocation.seat_value_changed()
