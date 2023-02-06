import math
from ElectionMethod import ElectionMethod


class LargestRemainderMethod(ElectionMethod):
    def __init__(self, _party_dict: dict[str, dict[str, int]], _seats: int, _options: dict[str, bool], _threshold: int,
                 _tag_along_seats: int, _added_value: int, _droop: bool):
        super().__init__(_party_dict, _seats, _options, _threshold, _tag_along_seats)
        self.added_value: int = _added_value
        self.droop: bool = _droop

    def calculate_seats(self, valid_vote_dict: dict[str, int] = None) -> dict[str, int]:
        seats_dict: dict[str, int] = self.gen_seats_dict(self.party_dict)
        remainder_dict: dict[str, float] = self.gen_remainder_dict(seats_dict)
        allocated_seats: float

        if valid_vote_dict is None:
            valid_vote_dict: dict[str, float] = self.remove_invalid_parties()

        if self.droop:
            quota: float = self.added_value + (sum(valid_vote_dict.values())) / (self.seats + self.added_value)
        else:
            quota: float = (sum(valid_vote_dict.values()) + self.added_value) / self.seats

        for party in valid_vote_dict.keys():
            allocated_seats = valid_vote_dict[party] / quota
            seats_dict[party] = math.floor(allocated_seats)
            remainder_dict[party] = allocated_seats - math.floor(allocated_seats)

        if len(seats_dict) > 1:
            for x in range(self.seats - sum(seats_dict.values())):
                seats_dict[max(remainder_dict, key=remainder_dict.get)] += 1
                remainder_dict.pop(max(remainder_dict, key=remainder_dict.get))

        return seats_dict
