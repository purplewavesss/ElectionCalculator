from Methods import Methods


class Settings:
    def __init__(self):
        self.method_type: bool = Methods.HIGHEST_AVERAGE_METHOD.value
        self.current_methods: dict[str, str] = {"highest_average": "d_hondt", "largest_remainder": "hare"}
        self.votes_forced = False
        self.forced_vote_num: int = 0

    def create_dict(self) -> dict:
        return {"method_type": self.method_type, "current_methods": self.current_methods, "votes_forced":
                self.votes_forced, "forced_vote_num": self.forced_vote_num}
