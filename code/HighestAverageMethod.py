import math
from ElectionMethod import ElectionMethod
from Settings import Settings


class HighestAverageMethod(ElectionMethod):
    def __init__(self, _party_dict: dict[str, dict[str, int]], _seats: int, _options: dict[str, bool], _threshold: int,
                 _tag_along_seats: int, _settings: Settings, _divisor: float, _huntington_hill: bool):
        super().__init__(_party_dict, _seats, _options, _threshold, _tag_along_seats, _settings)
        self.divisor: float = _divisor
        self.huntington_hill = _huntington_hill

    def calculate_seats(self, valid_vote_dict: dict[str, int] = None) -> dict[str, int]:
        """Returns dictionary of number of seats each party should qualify for"""
        seats_dict: dict[str, int] = self.gen_seats_dict(self.party_dict)
        valid_vote_dict: dict[str, float]

        if valid_vote_dict is None:
            valid_vote_dict = self.remove_invalid_parties()

        for x in range(self.seats):
            max_value = max(valid_vote_dict, key=valid_vote_dict.get)
            seats_dict[max_value] += 1
            valid_vote_dict[max_value] = self.vote_dict[max_value] / self.calculate_divider(seats_dict, max_value)

        return seats_dict

    def calculate_divider(self, seats_dict, max_value) -> float:
        if self.huntington_hill:
            return math.sqrt(seats_dict[max_value] * (seats_dict[max_value] + self.divisor))
        else:
            return seats_dict[max_value] + self.divisor
