from PyQt5 import QtWidgets
from gen_message_box import gen_message_box


class SeatAllocation:
    def __init__(self, _electorate_input: QtWidgets.QLineEdit, _list_input: QtWidgets.QLineEdit,
                 _total_input: QtWidgets.QLineEdit):
        self.electorate_input: QtWidgets.QLineEdit = _electorate_input
        self.list_input: QtWidgets.QLineEdit = _list_input
        self.total_input: QtWidgets.QLineEdit = _total_input
        self.__electorates: int = 0
        self.__list_seats: int = 0
        self.__total_seats: int = 0

    def get_electorates(self) -> int:
        return self.__electorates

    def set_electorates(self, _electorates: int):
        self.__electorates = _electorates
        self.electorate_input.setText(str(self.get_electorates()))

    def get_list_seats(self) -> int:
        return self.__list_seats

    def set_list_seats(self, _list_seats: int):
        self.__list_seats = _list_seats
        self.list_input.setText(str(self.get_list_seats()))

    def get_total_seats(self) -> int:
        return self.__total_seats

    def set_total_seats(self, _total_seats: int):
        self.__total_seats = _total_seats
        self.total_input.setText(str(self.get_total_seats()))

    def seat_value_changed(self) -> bool:
        """Changes total_input to value of both inputs, and returns whether calculation is possible"""
        button_enabled = False

        if self.electorate_input.text().isdecimal() and self.list_input.text().isdecimal():
            self.set_electorates(int(self.electorate_input.text()))
            self.set_list_seats(int(self.list_input.text()))
            self.set_total_seats(self.get_electorates() + self.get_list_seats())
            self.total_input.setText(str(self.get_electorates() + self.get_list_seats()))
            button_enabled = True

        elif (self.electorate_input.text() == "" and self.list_input.text().isdecimal()) or (
                self.list_input.text() == "" and self.electorate_input.text().isdecimal()):
            if self.electorate_input.text() == "":
                self.set_electorates(0)
                self.set_list_seats(int(self.list_input.text()))
                self.set_total_seats(self.get_list_seats())

            elif self.list_input.text() == "":
                self.set_electorates(int(self.electorate_input.text()))
                self.set_list_seats(0)
                self.set_total_seats(self.get_electorates())

            button_enabled = True

        else:
            gen_message_box("Invalid seat value", "Number of seats must be an integer.",
                            QtWidgets.QMessageBox.Icon.Warning)

        return button_enabled

    def total_seats_changed(self) -> bool:
        """Changes list_input to the difference of the other inputs, and returns whether calculation is possible"""
        button_enabled: bool = False

        if self.total_input.text().isdecimal():
            self.set_total_seats(int(self.total_input.text()))
            if self.get_total_seats() >= self.get_electorates():
                self.set_list_seats(self.get_total_seats() - self.get_electorates())
                button_enabled = True
            else:
                gen_message_box("Invalid seat value", "Total seats cannot be greater than number of electorates!",
                                QtWidgets.QMessageBox.Icon.Warning)

        else:
            gen_message_box("Invalid seat value", "Number of seats must be an integer.",
                            QtWidgets.QMessageBox.Icon.Warning)

        return button_enabled

    def create_dict(self) -> dict:
        return {"electorates": self.get_electorates(), "list": self.get_list_seats(), "total": self.get_total_seats()}
