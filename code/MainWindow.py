from PyQt5 import QtWidgets
from UiMainWindow import UiMainWindow


class MainWindow(QtWidgets.QMainWindow, UiMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_ui(self)

        # Process options
        self.has_threshold: bool = self.enable_threshold_option.isChecked()
        self.threshold: int = self.threshold_num.value()
        self.has_tag_along: bool = self.enable_tag_along_option.isChecked()
        self.tag_along_seats: int = self.tag_along_num.value()
        self.has_overhang: bool = self.enable_overhang_option.isChecked()
        self.has_levelling: bool = self.enable_levelling_option.isChecked()

        if not self.has_threshold:
            self.threshold_num.setDisabled(True)
        if not self.has_tag_along:
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

    def change_options(self, option: str, toggled_on: bool):
        match option:
            case "threshold":
                self.has_threshold = toggled_on
                self.threshold_num.setEnabled(toggled_on)
            case "tag_along":
                self.has_tag_along = toggled_on
                self.tag_along_num.setEnabled(toggled_on)
            case "overhang":
                self.has_overhang = toggled_on
            case "levelling":
                self.has_levelling = toggled_on

    def set_threshold(self):
        self.threshold = self.threshold_num.value()

    def set_tag_along(self):
        self.tag_along_seats = self.threshold_num.value()
