from enum import Enum

from settings import Settings


class EventType(Enum):
    SHIP_HIT = "SHIP_HIT"


class Stats:
    def __init__(self) -> None:
        self.ships_left = Settings().starting_ships

    def record(self, event: EventType):
        if event == EventType.SHIP_HIT:
            self.ships_left -= 1
