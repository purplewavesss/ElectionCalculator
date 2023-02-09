from abc import ABC, abstractmethod
from Settings import Settings


class ElectionMethod(ABC):
    def __init__(self, _party_dict: dict[str, dict[str, int]], _seats: int, _options: dict[str, bool],
                 _threshold: int, _tag_along_seats: int, _settings: Settings):
        self.party_dict: dict[str, dict[str, int]] = _party_dict
        self.vote_dict: dict[str, int] = self.gen_vote_dict(self.party_dict)
        self.seats: int = _seats
        self.options: dict[str, bool] = _options
        self.threshold = _threshold
        self.tag_along_seats = _tag_along_seats
        self.settings = _settings

    def remove_invalid_parties(self) -> dict[str, int]:
        """Checks if parties fail the threshold, and removes them if they do"""
        valid_dict: dict[str, int] = {}
        votes: int = self.calculate_votes(self.vote_dict, self.settings)

        if self.options["threshold"]:
            for key in self.vote_dict:
                if self.threshold_check(self.threshold, self.vote_dict[key], votes) or \
                        (self.party_dict[key]["electorates"] >= self.tag_along_seats and self.options["tag_along"]):
                    valid_dict.update({key: self.vote_dict[key]})
            return valid_dict
        return self.vote_dict.copy()

    def calculate_election(self, results: dict[str, int]) -> dict[str, dict[str, int]]:
        """Calculates and returns the number of electorates, list seats, and total seats for each party"""
        overhang_party_seats = 0
        overhang_parties: dict[str, int] = {}
        valid_vote_dict = self.remove_invalid_parties()

        # Checks and stores overhang seats
        for party in results.keys():
            if results[party] < self.party_dict[party]["electorates"]:
                results[party] = self.party_dict[party]["electorates"]
                overhang_party_seats += self.party_dict[party]["electorates"]
                overhang_parties.update({party: results[party]})

        # Removes list seats to account for overhang seats if needed
        # TODO: Fix levelling for parties that receive electorates seats without crossing the threshold
        if not self.options["overhang"]:
            self.seats -= overhang_party_seats
            for key in overhang_parties.keys():
                if key in valid_vote_dict.keys():
                    valid_vote_dict.pop(key)
            results = self.calculate_seats(valid_vote_dict)
            for key in overhang_parties.keys():
                results.update({key: overhang_parties[key]})
            self.seats += overhang_party_seats

        # Adds levelling seats if needed
        if self.options["levelling"] and overhang_party_seats > 0:
            self.seats = self.calculate_levelling(self.remove_invalid_parties(), results, self.seats)
            results = self.calculate_seats()

        # Updates the dictionary with information for each party
        for party in results.keys():
            self.party_dict[party].update({"list": results[party] - self.party_dict[party]["electorates"],
                                           "total": results[party]})

        return self.party_dict

    @abstractmethod
    def calculate_seats(self, valid_vote_dict: dict[str, int] = None) -> dict[str, int]:
        pass

    @staticmethod
    def calculate_levelling(vote_dict: dict[str, int], seats_dict: dict[str, int], seats: int) -> int:
        """Calculates number of seats with added levelling"""
        diff: float = 1

        # Calculate difference between number of seats and number of votes
        for party in seats_dict.keys():
            seats_percentage: float = seats_dict[party] / seats
            votes_percentage: float = vote_dict[party] / sum(vote_dict.values())
            diff = max(diff, (seats_percentage / votes_percentage))

        seats = int(seats * diff)
        return seats

    @staticmethod
    def calculate_votes(valid_vote_dict: dict[str, int], settings: Settings) -> int:
        if settings.votes_forced:
            votes = settings.forced_vote_num
            if votes < sum(valid_vote_dict.values()):
                # TODO: Add a dialog asking for the user to change their number of votes to something equal to or above
                # the current number of votes
                raise NotImplementedError
            else:
                return votes
        else:
            return sum(valid_vote_dict.values())

    @staticmethod
    def gen_vote_dict(party_dict: dict[str, dict[str, int]]) -> dict[str, int]:
        """Returns dictionary containing the number of votes each party obtained"""
        vote_dict: dict[str, int] = {}
        for key in party_dict.keys():
            vote_dict.update({key: party_dict[key]["votes"]})
        return vote_dict

    @staticmethod
    def gen_seats_dict(party_dict: dict[str, dict[str, int]]) -> dict[str, int]:
        """Creates dictionary of each party's number of seats, initialized to zero"""
        seats_dict: dict[str, int] = {}

        for key in party_dict.keys():
            seats_dict.update({key: 0})

        return seats_dict

    @staticmethod
    def gen_remainder_dict(valid_vote_dict: dict[str, int]) -> dict[str, float]:
        remainder_dict: dict[str, float] = {}

        for party in valid_vote_dict.keys():
            valid_vote_dict.update({party: 0})

        return remainder_dict

    @staticmethod
    def threshold_check(threshold: int, party_votes: int, total_votes: int) -> bool:
        if party_votes / total_votes >= (threshold / 100):
            return True
        return False
