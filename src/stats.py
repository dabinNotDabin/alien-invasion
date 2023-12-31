from enum import Enum


class EventType(Enum):
    SHIP_HIT = "SHIP_HIT"


class Stats:
    def __init__(self, starting_ships: int) -> None:
        self.ships_left = starting_ships
        self.score = 0

    def record(self, event: EventType):
        if event == EventType.SHIP_HIT:
            self.ships_left -= 1

    def increment_score(self, amount: int):
        self.score += amount
