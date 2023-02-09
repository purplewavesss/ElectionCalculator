import json
import os

from PyQt5 import QtWidgets
from UiMainWindow import UiMainWindow
from ElectionMethodFactory import ElectionMethodFactory
from gen_message_box import gen_message_box


class MainWindow(QtWidgets.QMainWindow, UiMainWindow):
    # TODO: Prompt user to save if they exit
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
            results = method.calculate_election(method.calculate_seats())

            self.election_table.display_election(results)

        else:
            gen_message_box("Invalid electorate number!", "The number of electorates for the election does not match "
                                                          "the number of electorates earned by parties.",
                                                          QtWidgets.QMessageBox.Icon.Warning)

    def set_options(self, _options: dict[str, dict]):
        self.options = _options["names"]
        self.threshold_num.setValue(_options["values"]["threshold_num"])
        self.set_threshold()
        self.tag_along_num.setValue(_options["values"]["tag_along_num"])
        self.set_tag_along()

        # Set group box items
        for group_box in (self.levelling_box, self.overhang_box, self.tag_along_box, self.threshold_box):
            for radio_button in group_box.children():
                if isinstance(radio_button, QtWidgets.QRadioButton):
                    name_list: list[str] = radio_button.objectName().split("_")
                    name: str = ""

                    for x in range(len(name_list)):
                        if x != 0:
                            name += (name_list[x])
                            if x != len(name_list) - 1:
                                name += "_"

                    if name_list[0] == "enable":
                        radio_button.setChecked(self.options[name])
                    else:
                        radio_button.setChecked(not self.options[name])

    def get_options_dict(self) -> dict[str, dict]:
        return {"names": self.options, "values": {"threshold_num": self.threshold, "tag_along_num":
                self.tag_along_seats}}

    def read_json(self, file_path: str):
        election: dict[str, dict]
        parties: int

        with open(file_path, "r") as json_file:
            election = json.loads(json_file.read())

        try:
            # Import election results
            self.election_table.clear_table()
            self.election_table.setRowCount(len(election["parties"].keys()) + 1)
            self.election_table.add_header()
            self.election_table.display_election(election["parties"])

            # Import seat allocation
            self.seat_allocation.set_electorates(election["allocation"]["electorates"])
            self.seat_allocation.set_list_seats(election["allocation"]["list"])
            self.seat_allocation.set_total_seats(election["allocation"]["total"])

            # Import settings
            self.settings.method_type = election["settings"]["method_type"]
            self.settings.current_methods = election["settings"]["current_methods"]
            self.settings.votes_forced = election["settings"]["votes_forced"]
            self.settings.forced_vote_num = election["settings"]["forced_vote_num"]

            # Import options
            self.set_options(election["options"])

        except KeyError:
            gen_message_box("Invalid JSON File!", "The JSON file imported does not contain a valid election. Use "
                                                  "election.json as a blueprint to create a valid one.",
                            QtWidgets.QMessageBox.Icon.Critical)

    def save_json(self, file_path: str):
        file_action: str

        if os.path.isfile(file_path):
            file_action = "w"

        else:
            file_action = "x"

        with open(file_path, file_action) as json_file:
            json_file.write(json.dumps({"parties": self.election_table.generate_party_dict(),
                                        "settings": self.settings.create_dict(),
                                        "allocation": self.seat_allocation.create_dict(),
                                        "options": self.get_options_dict()}, indent=4))
