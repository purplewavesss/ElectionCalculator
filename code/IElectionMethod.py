class IElectionMethod:
    def calculate_seats(self) -> dict[str, int]:
        pass

    def threshold_check(self) -> bool:
        pass

    def calculate_list_seat_num(self) -> int:
        pass
