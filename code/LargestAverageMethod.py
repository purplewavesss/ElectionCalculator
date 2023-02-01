from ElectionMethod import ElectionMethod


class LargestAverageMethod(ElectionMethod):
    def __init__(self, _party_dict: dict[str, dict[str, int]], _seats: int, _divisor: float, _options: dict[str, bool],
                 _threshold: int, _tag_along_seats: int):
        self.party_dict: dict[str, dict[str, int]] = _party_dict
        self.vote_dict: dict[str, int] = self.gen_vote_dict(self.party_dict)
        self.seats: int = _seats
        self.divisor: float = _divisor
        self.options: dict[str, bool] = _options
        self.threshold = _threshold
        self.tag_along_seats = _tag_along_seats

    def calculate_seats(self) -> dict[str, int]:
        results: dict[str, int] = self.gen_seats_dict(self.party_dict)
        lam_vote_dict: dict[str, float] = self.remove_invalid_parties()

        for x in range(self.seats):
            max_value = max(lam_vote_dict, key=lam_vote_dict.get)
            results[max_value] += 1
            lam_vote_dict[max_value] = self.vote_dict[max_value] / ((results[max_value] * self.divisor) + 1)

        return results

    def remove_invalid_parties(self) -> dict[str, int]:
        valid_dict: dict[str, int] = {}
        if self.options["threshold"]:
            for key in self.vote_dict:
                if self.threshold_check(self.threshold, self.vote_dict[key], sum(self.vote_dict.values())) or \
                        (self.party_dict[key]["electorates"] >= self.tag_along_seats and self.options["tag_along"]):
                    valid_dict.update({key: self.vote_dict[key]})
            return valid_dict
        return self.vote_dict.copy()

    def calculate_list_seat_num(self) -> int:
        pass
