from Methods import Methods


class Settings:
    def __init__(self):
        self.method_type = Methods.HIGHEST_AVERAGE_METHOD.value
        self.current_methods: dict[str, str] = {"highest_average": "d_hondt", "largest_remainder": "hare"}
        self.votes_forced = False
        self.forced_vote_num: int = 0
