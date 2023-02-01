import math
from abc import ABC, abstractmethod


class ElectionMethod(ABC):
    def __init__(self, _party_dict: dict[str, dict[str, int]], _seats: int, _options: dict[str, bool],
                 _threshold: int, _tag_along_seats: int):
        self.party_dict: dict[str, dict[str, int]] = _party_dict
        self.vote_dict: dict[str, int] = self.gen_vote_dict(self.party_dict)
        self.seats: int = _seats
        self.options: dict[str, bool] = _options
        self.threshold = _threshold
        self.tag_along_seats = _tag_along_seats

    def remove_invalid_parties(self) -> dict[str, int]:
        valid_dict: dict[str, int] = {}
        if self.options["threshold"]:
            for key in self.vote_dict:
                if self.threshold_check(self.threshold, self.vote_dict[key], sum(self.vote_dict.values())) or \
                        (self.party_dict[key]["electorates"] >= self.tag_along_seats and self.options["tag_along"]):
                    valid_dict.update({key: self.vote_dict[key]})
            return valid_dict
        return self.vote_dict.copy()

    def calculate_party_dict(self, results: dict[str, int]) -> dict[str, dict[str, int]]:
        overhang_party_seats = 0
        overhang_parties: dict[str, int] = {}
        valid_vote_dict = self.remove_invalid_parties()

        for party in results.keys():
            if results[party] < self.party_dict[party]["electorates"]:
                results[party] = self.party_dict[party]["electorates"]
                overhang_party_seats += self.party_dict[party]["electorates"]
                overhang_parties.update({party: results[party]})

        if not self.options["overhang"] and not self.options["levelling"]:
            self.seats -= overhang_party_seats
            for key in overhang_parties.keys():
                valid_vote_dict.pop(key)
            results = self.calculate_seats(valid_vote_dict)
            for key in overhang_parties.keys():
                results.update({key: overhang_parties[key]})

        elif self.options["levelling"] and overhang_party_seats:
            self.seats = self.calculate_levelling(self.remove_invalid_parties(), results, self.seats)
            results = self.calculate_seats()

        for party in results.keys():
            self.party_dict[party].update({"list": results[party] - self.party_dict[party]["electorates"],
                                           "total_seats": results[party]})

        return self.party_dict

    @abstractmethod
    def calculate_seats(self, valid_vote_dict: dict[str, float] = None) -> dict[str, int]:
        pass

    @staticmethod
    def calculate_levelling(vote_dict: dict[str, int], seats_dict: dict[str, int], seats: int) -> int:
        diff: float = 1.00000
        for party in seats_dict.keys():
            seats_percentage: float = seats_dict[party] / sum(seats_dict.values())
            votes_percentage: float = vote_dict[party] / sum(vote_dict.values())
            diff = max(diff, (seats_percentage / votes_percentage))
        seats = math.ceil(seats * diff)
        return seats

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
