from Settings import Settings
from ElectionMethod import ElectionMethod
from HighestAverageMethod import HighestAverageMethod
from LargestRemainderMethod import LargestRemainderMethod


class ElectionMethodFactory:
    def __init__(self, _party_dict: dict[str, dict[str, int]], _seats: int, _options: dict[str, bool], _threshold: int,
                 _tag_along_seats: int, _settings: Settings):
        self.party_dict: dict[str, dict[str, int]] = _party_dict
        self.seats: int = _seats
        self.options: dict[str, bool] = _options
        self.threshold = _threshold
        self.tag_along_seats = _tag_along_seats
        self.settings = _settings

    def create_election_method(self) -> ElectionMethod:
        if self.settings.method_type:
            match self.settings.current_methods["highest_average"]:
                case "d_hondt":
                    return HighestAverageMethod(self.party_dict, self.seats, self.options, self.threshold,
                                                self.tag_along_seats, 1, self.settings)
                case "sainte_lague":
                    return HighestAverageMethod(self.party_dict, self.seats, self.options, self.threshold,
                                                self.tag_along_seats, 0.5, self.settings)
                case "huntington_hill":
                    raise NotImplementedError

                case "imperiali_ham":
                    return HighestAverageMethod(self.party_dict, self.seats, self.options, self.threshold,
                                                self.tag_along_seats, 2, self.settings)
        else:
            match self.settings.current_methods["largest_remainder"]:
                case "hare":
                    return LargestRemainderMethod(self.party_dict, self.seats, self.options, self.threshold,
                                                  self.tag_along_seats, 0, False, self.settings)
                case "droop":
                    return LargestRemainderMethod(self.party_dict, self.seats, self.options, self.threshold,
                                                  self.tag_along_seats, 1, True, self.settings)
                case "hagenbach":
                    return LargestRemainderMethod(self.party_dict, self.seats, self.options, self.threshold,
                                                  self.tag_along_seats, 1, False, self.settings)
                case "imperiali_lrm":
                    return LargestRemainderMethod(self.party_dict, self.seats, self.options, self.threshold,
                                                  self.tag_along_seats, 2, False, self.settings)
