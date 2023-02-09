import json
import os
from PyQt5 import QtWidgets
from Settings import Settings
from SeatAllocation import SeatAllocation
from ElectionTable import ElectionTable
from MainWindow import MainWindow
from gen_message_box import gen_message_box


def read_json(file_path: str, main_window: MainWindow):
    election: dict[str, dict]
    parties: int

    with open(file_path, "r") as json_file:
        election = json.loads(json_file.read())

    try:
        # Import election results
        main_window.election_table.clear_table()
        main_window.election_table.setRowCount(len(election["parties"].keys()) + 1)
        main_window.election_table.add_header()
        main_window.election_table.display_election(election["parties"])

        # Import seat allocation
        main_window.seat_allocation.set_electorates(election["allocation"]["electorates"])
        main_window.seat_allocation.set_list_seats(election["allocation"]["list"])
        main_window.seat_allocation.set_total_seats(election["allocation"]["total"])

        # Import settings
        main_window.settings.method_type = election["settings"]["method_type"]
        main_window.settings.current_methods = election["settings"]["current_methods"]
        main_window.settings.votes_forced = election["settings"]["votes_forced"]
        main_window.settings.forced_vote_num = election["settings"]["forced_vote_num"]

        # Import options
        main_window.set_options(election["options"])

    except KeyError:
        gen_message_box("Invalid JSON File!", "The JSON file imported does not contain a valid election. Use "
                        "election.json as a blueprint to create a valid one.", QtWidgets.QMessageBox.Icon.Critical)


def save_json(file_path: str, election_table: ElectionTable, settings: Settings, seat_allocation: SeatAllocation):
    if os.path.isfile(file_path):
        with open(file_path, "w") as json_file:
            json_file.write(json.dumps({"parties": election_table.generate_party_dict(),
                                        "settings": settings.create_dict(),
                                        "allocation": seat_allocation.create_dict()}))
