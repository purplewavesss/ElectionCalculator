# Form implementation generated from reading ui file 'mainwindow.ui'
from PyQt5 import QtCore, QtWidgets
from ElectionTable import ElectionTable


class UiMainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(610, 420)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.election_table = ElectionTable(self.central_widget, QtCore.QRect(10, 10, 410, 320), 1, 5, False)
        self.append_party_table = ElectionTable(self.central_widget, QtCore.QRect(10, 340, 250, 40), 1, 3, True)
        self.plus_button = QtWidgets.QPushButton(self.central_widget)
        self.plus_button.setGeometry(QtCore.QRect(270, 340, 70, 40))
        self.plus_button.setObjectName("plus_button")
        self.minus_button = QtWidgets.QPushButton(self.central_widget)
        self.minus_button.setGeometry(QtCore.QRect(350, 340, 70, 40))
        self.minus_button.setObjectName("minus_button")
        self.threshold_box = QtWidgets.QGroupBox(self.central_widget)
        self.threshold_box.setGeometry(QtCore.QRect(425, 10, 80, 80))
        self.threshold_box.setObjectName("threshold_box")
        self.no_threshold_option = QtWidgets.QRadioButton(self.threshold_box)
        self.no_threshold_option.setGeometry(QtCore.QRect(10, 20, 60, 20))
        self.no_threshold_option.setChecked(True)
        self.no_threshold_option.setObjectName("no_threshold_option")
        self.enable_threshold_option = QtWidgets.QRadioButton(self.threshold_box)
        self.enable_threshold_option.setGeometry(QtCore.QRect(10, 50, 60, 20))
        self.enable_threshold_option.setText("")
        self.enable_threshold_option.setObjectName("enable_threshold_option")
        self.threshold_num = QtWidgets.QSpinBox(self.threshold_box)
        self.threshold_num.setGeometry(QtCore.QRect(30, 50, 40, 20))
        self.threshold_num.setMinimum(1)
        self.threshold_num.setObjectName("threshold_num")
        self.tag_along_box = QtWidgets.QGroupBox(self.central_widget)
        self.tag_along_box.setGeometry(QtCore.QRect(515, 10, 80, 80))
        self.tag_along_box.setObjectName("tag_along_box")
        self.disable_tag_along_option = QtWidgets.QRadioButton(self.tag_along_box)
        self.disable_tag_along_option.setGeometry(QtCore.QRect(10, 20, 70, 20))
        self.disable_tag_along_option.setChecked(True)
        self.disable_tag_along_option.setObjectName("disable_tag_along_option")
        self.enable_tag_along_option = QtWidgets.QRadioButton(self.tag_along_box)
        self.enable_tag_along_option.setGeometry(QtCore.QRect(10, 50, 60, 20))
        self.enable_tag_along_option.setText("")
        self.enable_tag_along_option.setObjectName("enable_tag_along_option")
        self.tag_along_num = QtWidgets.QSpinBox(self.tag_along_box)
        self.tag_along_num.setGeometry(QtCore.QRect(30, 50, 40, 20))
        self.tag_along_num.setMinimum(1)
        self.tag_along_num.setObjectName("tag_along_num")
        self.overhang_box = QtWidgets.QGroupBox(self.central_widget)
        self.overhang_box.setGeometry(QtCore.QRect(425, 100, 80, 80))
        self.overhang_box.setObjectName("overhang_box")
        self.disable_overhang_option = QtWidgets.QRadioButton(self.overhang_box)
        self.disable_overhang_option.setGeometry(QtCore.QRect(10, 20, 70, 20))
        self.disable_overhang_option.setChecked(True)
        self.disable_overhang_option.setObjectName("disable_overhang_option")
        self.enable_overhang_option = QtWidgets.QRadioButton(self.overhang_box)
        self.enable_overhang_option.setGeometry(QtCore.QRect(10, 50, 70, 20))
        self.enable_overhang_option.setObjectName("enable_overhang_option")
        self.levelling_box = QtWidgets.QGroupBox(self.central_widget)
        self.levelling_box.setGeometry(QtCore.QRect(515, 100, 80, 80))
        self.levelling_box.setObjectName("levelling_box")
        self.disable_levelling_option = QtWidgets.QRadioButton(self.levelling_box)
        self.disable_levelling_option.setGeometry(QtCore.QRect(10, 20, 70, 20))
        self.disable_levelling_option.setChecked(True)
        self.disable_levelling_option.setObjectName("disable_levelling_option")
        self.enable_levelling_option = QtWidgets.QRadioButton(self.levelling_box)
        self.enable_levelling_option.setGeometry(QtCore.QRect(10, 50, 70, 20))
        self.enable_levelling_option.setObjectName("enable_levelling_option")
        self.electorate_input = QtWidgets.QLineEdit(self.central_widget)
        self.electorate_input.setGeometry(QtCore.QRect(505, 210, 95, 20))
        self.electorate_input.setObjectName("electorate_input")
        self.electorate_label = QtWidgets.QLabel(self.central_widget)
        self.electorate_label.setGeometry(QtCore.QRect(430, 210, 65, 20))
        self.electorate_label.setObjectName("electorate_label")
        self.list_input = QtWidgets.QLineEdit(self.central_widget)
        self.list_input.setGeometry(QtCore.QRect(505, 240, 95, 20))
        self.list_input.setObjectName("list_input")
        self.list_label = QtWidgets.QLabel(self.central_widget)
        self.list_label.setGeometry(QtCore.QRect(430, 240, 65, 20))
        self.list_label.setObjectName("list_label")
        self.clear_button = QtWidgets.QPushButton(self.central_widget)
        self.clear_button.setGeometry(QtCore.QRect(430, 310, 170, 30))
        self.clear_button.setObjectName("clear_button")
        self.calculate_button = QtWidgets.QPushButton(self.central_widget)
        self.calculate_button.setGeometry(QtCore.QRect(430, 350, 170, 30))
        self.calculate_button.setObjectName("calculate_button")
        main_window.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 610, 26))
        self.menu_bar.setObjectName("menu_bar")
        self.file_menu = QtWidgets.QMenu(self.menu_bar)
        self.file_menu.setObjectName("file_menu")
        self.help_menu = QtWidgets.QMenu(self.menu_bar)
        self.help_menu.setObjectName("help_menu")
        main_window.setMenuBar(self.menu_bar)
        self.open_action = QtWidgets.QAction(main_window)
        self.open_action.setObjectName("open_action")
        self.about_action = QtWidgets.QAction(main_window)
        self.about_action.setObjectName("about_action")
        self.save_action = QtWidgets.QAction(main_window)
        self.save_action.setObjectName("save_action")
        self.exit_action = QtWidgets.QAction(main_window)
        self.exit_action.setObjectName("exit_action")
        self.settings_action = QtWidgets.QAction(main_window)
        self.settings_action.setObjectName("settings_action")
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.settings_action)
        self.file_menu.addAction(self.exit_action)
        self.help_menu.addAction(self.about_action)
        self.menu_bar.addAction(self.file_menu.menuAction())
        self.menu_bar.addAction(self.help_menu.menuAction())

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        self.set_actions()

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Election Calculator"))
        item = self.election_table.verticalHeaderItem(0)
        item.setText(_translate("main_window", "label_row"))
        item = self.election_table.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "party_names_column"))
        item = self.election_table.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "votes_column"))
        item = self.election_table.horizontalHeaderItem(2)
        item.setText(_translate("main_window", "electorates_column"))
        item = self.election_table.horizontalHeaderItem(3)
        item.setText(_translate("main_window", "list_seats_column"))
        item = self.election_table.horizontalHeaderItem(4)
        item.setText(_translate("main_window", "total_seats_column"))
        __sortingEnabled = self.election_table.isSortingEnabled()
        self.election_table.setSortingEnabled(False)
        item = self.election_table.item(0, 0)
        item.setText(_translate("main_window", "Party Name:"))
        item = self.election_table.item(0, 1)
        item.setText(_translate("main_window", "# of votes:"))
        item = self.election_table.item(0, 2)
        item.setText(_translate("main_window", "# of electorates:"))
        item = self.election_table.item(0, 3)
        item.setText(_translate("main_window", "# of list seats:"))
        item = self.election_table.item(0, 4)
        item.setText(_translate("main_window", "# of total seats:"))
        self.election_table.setSortingEnabled(__sortingEnabled)
        item = self.append_party_table.verticalHeaderItem(0)
        item.setText(_translate("main_window", "input_row"))
        item = self.append_party_table.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "party_name_column"))
        item = self.append_party_table.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "votes_column"))
        item = self.append_party_table.horizontalHeaderItem(2)
        item.setText(_translate("main_window", "electorates_column"))
        __sortingEnabled = self.append_party_table.isSortingEnabled()
        self.append_party_table.setSortingEnabled(False)
        self.append_party_table.setSortingEnabled(__sortingEnabled)
        self.plus_button.setText(_translate("main_window", "+"))
        self.minus_button.setText(_translate("main_window", "-"))
        self.threshold_box.setTitle(_translate("main_window", "Threshold"))
        self.no_threshold_option.setText(_translate("main_window", "None"))
        self.tag_along_box.setTitle(_translate("main_window", "Tag-along"))
        self.disable_tag_along_option.setText(_translate("main_window", "Disable"))
        self.overhang_box.setTitle(_translate("main_window", "Overhang"))
        self.disable_overhang_option.setText(_translate("main_window", "Disable"))
        self.enable_overhang_option.setText(_translate("main_window", "Enable"))
        self.levelling_box.setTitle(_translate("main_window", "Levelling"))
        self.disable_levelling_option.setText(_translate("main_window", "Disable"))
        self.enable_levelling_option.setText(_translate("main_window", "Enable"))
        self.electorate_label.setText(_translate("main_window", "Electorates"))
        self.list_label.setText(_translate("main_window", "List Seats"))
        self.clear_button.setText(_translate("main_window", "Clear"))
        self.calculate_button.setText(_translate("main_window", "Calculate"))
        self.file_menu.setTitle(_translate("main_window", "File"))
        self.help_menu.setTitle(_translate("main_window", "Help"))
        self.settings_action.setText(_translate("main_window", "Settings"))
        self.open_action.setText(_translate("main_window", "Open"))
        self.about_action.setText(_translate("main_window", "About"))
        self.save_action.setText(_translate("main_window", "Save"))
        self.exit_action.setText(_translate("main_window", "Exit"))

    def set_actions(self):
        self.plus_button.clicked.connect(lambda: self.election_table.append_row(self.append_party_table))
        self.minus_button.clicked.connect(self.election_table.delete_row)
        self.clear_button.clicked.connect(self.election_table.clear_table)
