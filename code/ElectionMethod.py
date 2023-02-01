from abc import ABC, abstractmethod


class ElectionMethod(ABC):
    @abstractmethod
    def calculate_seats(self) -> dict[str, int]:
        pass

    @abstractmethod
    def calculate_list_seat_num(self) -> int:
        pass

    @staticmethod
    def gen_vote_dict(party_dict: dict[str, dict[str, int]]) -> dict[str, int]:
        vote_dict: dict[str, int] = {}
        for key in party_dict.keys():
            vote_dict.update({key: party_dict[key]["votes"]})
        return vote_dict

    @staticmethod
    def gen_seats_dict(party_dict: dict[str, dict[str, int]]) -> dict[str, int]:
        seats_dict: dict[str, int] = {}

        for key in party_dict.keys():
            seats_dict.update({key: 0})

        return seats_dict

    @staticmethod
    def threshold_check(threshold: float, party_votes: int, total_votes: int) -> bool:
        if party_votes / total_votes >= threshold:
            return True
        return False
