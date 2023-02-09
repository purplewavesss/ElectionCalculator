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
            self.itemClicked.connect(self.item_clicked)  # type: ignore

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

    def append_row(self, table_row: QtWidgets.QTableWidget) -> bool:
        """Adds a one-row table to an election table"""
        # Remove commas from input
        for x in range(table_row.columnCount()):
            table_row.item(0, x).setText(re.sub(",", "", table_row.item(0, x).text()))

        # Zero out empty values
        if (table_row.item(0, Columns.ELECTORATE.value).text() or table_row.item(0, Columns.TOTAL.value).text()) \
                == "":
            table_row.item(0, Columns.ELECTORATE.value).setText("0")

        # Check if input is valid for row added
        # TODO: Account for more possibilities
        if str(table_row.item(0, Columns.VOTES.value).text()).isdecimal() and \
                str(table_row.item(0, Columns.ELECTORATE.value).text()).isdecimal():
            row_position = self.rowCount()

            # Insert and fill row
            self.insertRow(row_position)
            for x in range(self.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                self.setItem(row_position, x, item)
                if x < table_row.columnCount():
                    self.item(row_position, x).setText(table_row.item(0, x).text())

                # Check if items are editable
                if x <= Columns.ELECTORATE.value:
                    self.edit_dict.update({(row_position, x): True})
                else:
                    self.edit_dict.update({(row_position, x): False})

            # Add to table_electorates
            self.table_electorates += int(table_row.item(0, Columns.ELECTORATE.value).text())
            self.electorate_increase()
            return True

        else:
            gen_message_box("Invalid input!", "Votes and electorates must be integers.",
                            QtWidgets.QMessageBox.Icon.Warning)
            return False

    def delete_row(self):
        if self.rowCount() > 1:
            deleted_row: int = self.rowCount() - 1
            self.table_electorates -= int(self.item(deleted_row, Columns.ELECTORATE.value).text())
            self.removeRow(deleted_row)
            for x in range(self.columnCount()):
                if (deleted_row, x) in self.edit_dict.keys():
                    self.edit_dict.pop((deleted_row, x))

    def generate_edit_dict(self):
        """Generates a dictionary determining whether items are editable"""
        for x in range(self.rowCount()):
            for y in range(self.columnCount()):
                if y <= Columns.ELECTORATE.value and x != 0:
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
                # Creates a dict of {party_name: {votes, electorates, list, total}}
                party_dict.update({self.item(x, Columns.PARTY.value).text():
                                  {"votes": int(self.item(x, Columns.VOTES.value).text()),
                                   "electorates": int(self.item(x, Columns.ELECTORATE.value).text())}})

                if self.item(x, Columns.LIST.value).text():
                    party_dict[self.item(x, Columns.PARTY.value).text()].update({
                        "list": int(self.item(x, Columns.LIST.value).text())})

                if self.item(x, Columns.TOTAL.value).text():
                    party_dict[self.item(x, Columns.PARTY.value).text()].update({
                        "total": int(self.item(x, Columns.TOTAL.value).text())})
        return party_dict

    def set_value(self, rows: int, columns: int, text: str):
        item = QtWidgets.QTableWidgetItem()
        item.setText(text)
        self.setItem(rows, columns, item)

    def item_clicked(self, item: QtWidgets.QTableWidgetItem):
        if (item.row(), item.column()) in self.edit_dict:
            if self.edit_dict[(item.row(), item.column())]:
                if item.column() == Columns.PARTY.value:
                    change_item_dialog = ChangeItemDialog(item, False)
                else:
                    change_item_dialog = ChangeItemDialog(item, True)
                change_item_dialog.exec()

    def electorate_increase(self):
        try:
            if self.table_electorates > self.seat_allocation.get_electorates():
                self.seat_allocation.set_electorates(self.table_electorates)
                self.seat_allocation.seat_value_changed()
        except ValueError:
            self.seat_allocation.set_electorates(self.table_electorates)
            self.seat_allocation.seat_value_changed()

    def display_election(self, results: dict[str, dict[str, int]]):
        parties: list[str] = list(results.keys())

        for x in range(self.rowCount()):
            if x != 0:
                self.set_value(x, Columns.PARTY.value, parties[x - 1])
                self.set_value(x, Columns.VOTES.value, str(results[parties[x - 1]]["votes"]))
                self.set_value(x, Columns.ELECTORATE.value, str(results[parties[x - 1]]["electorates"]))
                self.set_value(x, Columns.LIST.value, str(results[parties[x - 1]]["list"]))
                self.set_value(x, Columns.TOTAL.value, str(results[parties[x - 1]]["total"]))

    def add_header(self):
        self.set_value(0, Columns.PARTY.value, "Party Name:")
        self.set_value(0, Columns.VOTES.value, "# of votes:")
        self.set_value(0, Columns.ELECTORATE.value, "# of electorates:")
        self.set_value(0, Columns.LIST.value, "# of list seats:")
        self.set_value(0, Columns.TOTAL.value, "# of total seats:")
