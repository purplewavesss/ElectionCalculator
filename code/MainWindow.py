from PyQt5 import QtWidgets
from UiMainWindow import UiMainWindow
from Columns import Columns
from ElectionMethodFactory import ElectionMethodFactory
from gen_message_box import gen_message_box


class MainWindow(QtWidgets.QMainWindow, UiMainWindow):
    def __init__(self, _settings):
        super(MainWindow, self).__init__()
        self.setup_ui(self)
        self.settings = _settings

        # Process options
        self.options: dict[str, bool] = {"threshold": self.enable_threshold_option.isChecked(),
                                         "tag_along": self.enable_tag_along_option.isChecked(),
                                         "overhang": self.enable_overhang_option.isChecked(),
                                         "levelling": self.enable_levelling_option.isChecked()}
        self.threshold: int = self.threshold_num.value()
        self.tag_along_seats: int = self.tag_along_num.value()

        self.connect_objects()

    def connect_objects(self):
        if not self.options["threshold"]:
            self.threshold_num.setDisabled(True)
        if not self.options["tag_along"]:
            self.tag_along_num.setDisabled(True)

        # Connect to change_options
        self.disable_threshold_option.toggled.connect(lambda: self.change_options("threshold", False))
        self.enable_threshold_option.toggled.connect(lambda: self.change_options("threshold", True))
        self.disable_tag_along_option.toggled.connect(lambda: self.change_options("tag_along", False))
        self.enable_tag_along_option.toggled.connect(lambda: self.change_options("tag_along", True))
        self.disable_overhang_option.toggled.connect(lambda: self.change_options("overhang", False))
        self.enable_overhang_option.toggled.connect(lambda: self.change_options("overhang", True))
        self.disable_levelling_option.toggled.connect(lambda: self.change_options("levelling", False))
        self.enable_levelling_option.toggled.connect(lambda: self.change_options("levelling", True))

        # Connect spin boxes to value variables
        self.threshold_num.valueChanged.connect(self.set_threshold)
        self.tag_along_num.valueChanged.connect(self.set_tag_along)
        self.calculate_button.clicked.connect(self.calculate)

        # Connect line edits to triggers
        self.electorate_input.editingFinished.connect(lambda: self.calculate_button.setEnabled(
            self.seat_allocation.seat_value_changed()))
        self.list_input.editingFinished.connect(lambda: self.calculate_button.setEnabled(
            self.seat_allocation.seat_value_changed()))
        self.total_input.editingFinished.connect(lambda: self.calculate_button.setEnabled(
            self.seat_allocation.total_seats_changed()))

        self.calculate_button.setDisabled(True)

    def change_options(self, option: str, toggled_on: bool):
        """Switches option based on user input"""
        self.options[option] = toggled_on

        # Switch on and off options based on the option changed
        match option:
            case "threshold":
                self.threshold_num.setEnabled(toggled_on)
            case "tag_along":
                self.tag_along_num.setEnabled(toggled_on)
            case "overhang":
                if toggled_on:
                    self.enable_levelling_option.setChecked(not toggled_on)
                    self.disable_levelling_option.setChecked(toggled_on)
                    self.options["levelling"] = not toggled_on
            case "levelling":
                if toggled_on:
                    self.enable_overhang_option.setChecked(not toggled_on)
                    self.disable_overhang_option.setChecked(toggled_on)
                    self.options["overhang"] = not toggled_on
            case _:
                raise ValueError("Incorrect option choice!")

    def set_threshold(self):
        self.threshold = self.threshold_num.value()

    def set_tag_along(self):
        self.tag_along_seats = self.tag_along_num.value()

    def calculate(self):
        """Calculates and displays election results"""
        election_data: dict[str, dict[str, int]] = self.election_table.generate_party_dict()
        electorates: int = 0
        election_method_factory = ElectionMethodFactory(election_data, self.seat_allocation.get_total_seats(),
                                                        self.options, self.threshold, self.tag_along_seats,
                                                        self.settings)

        for party in election_data.values():
            electorates += party["electorates"]

        # Run elections
        if self.seat_allocation.get_electorates() == electorates:
            method = election_method_factory.create_election_method()
            seats_dict = method.calculate_seats()
            results = method.calculate_party_dict(seats_dict)

            # Show results in table
            for x in range(self.election_table.rowCount()):
                if x != 0:
                    self.election_table.set_value(x, Columns.LIST.value,
                                                  str(results[self.election_table.item(x, 0).text()]["list"]))
                    self.election_table.set_value(x, Columns.TOTAL.value,
                                                  str(results[self.election_table.item(x, 0).text()]["total"]))

        else:
            gen_message_box("Invalid electorate number!", "The number of electorates for the election does not match "
                                                          "the number of electorates earned by parties.",
                                                          QtWidgets.QMessageBox.Icon.Warning)
