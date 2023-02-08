import json
from PyQt5 import QtWidgets
from Settings import Settings
from SeatAllocation import SeatAllocation
from ElectionTable import ElectionTable
from gen_message_box import gen_message_box


def json_parse(file_path: str, election_table: ElectionTable, settings: Settings, seat_allocation: SeatAllocation):
    election: dict[str, dict]
    parties: int

    with open(file_path, "r") as json_file:
        election = json.loads(json_file.read())

    try:
        # Import election results
        election_table.clear_table()
        election_table.setRowCount(len(election["parties"].keys()) + 1)
        election_table.add_header()
        election_table.display_election(election["parties"])

        # Import seat allocation
        seat_allocation.set_electorates(election["allocation"]["electorates"])
        seat_allocation.set_list_seats(election["allocation"]["list"])
        seat_allocation.set_total_seats(election["allocation"]["total"])

        # Import settings
        settings.method_type = election["settings"]["method_type"]
        settings.current_methods = election["settings"]["current_methods"]
        settings.votes_forced = election["settings"]["votes_forced"]
        settings.forced_vote_num = election["settings"]["forced_vote_num"]

    except KeyError:
        gen_message_box("Invalid JSON File!", "The JSON file imported does not contain a valid election. Use "
                        "election.json as a blueprint to create a valid one.", QtWidgets.QMessageBox.Icon.Critical)
