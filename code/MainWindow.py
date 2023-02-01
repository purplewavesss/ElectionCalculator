from PyQt5 import QtWidgets
from UiMainWindow import UiMainWindow
from LargestAverageMethod import LargestAverageMethod


class MainWindow(QtWidgets.QMainWindow, UiMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_ui(self)

        # Process options
        self.options: dict[str, bool] = {"threshold": self.enable_threshold_option.isChecked(),
                                              "tag_along": self.enable_tag_along_option.isChecked(),
                                              "overhang": self.enable_overhang_option.isChecked(),
                                              "levelling": self.enable_levelling_option.isChecked()}
        self.threshold: int = self.threshold_num.value()
        self.tag_along_seats: int = self.tag_along_num.value()

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

    def change_options(self, option: str, toggled_on: bool):
        self.options[option] = toggled_on

        match option:
            case "threshold":
                self.threshold_num.setEnabled(toggled_on)
            case "tag_along":
                self.tag_along_num.setEnabled(toggled_on)
            case _:
                pass

    def set_threshold(self):
        self.threshold = self.threshold_num.value() / 100

    def set_tag_along(self):
        self.tag_along_seats = self.threshold_num.value()

    def calculate(self):
        dhondt = LargestAverageMethod(self.election_table.generate_party_dict(), (int(self.electorate_input.text()) +
                                      int(self.list_input.text())), 1, self.options, self.threshold,
                                      self.tag_along_seats)
        print(dhondt.calculate_seats())
