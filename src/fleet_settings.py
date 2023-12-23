import enum


class FleetSettings:
    def __init__(self) -> None:
        self.direction = FleetDirection.RIGHT


class FleetDirection(enum.IntEnum):
    LEFT = -1
    RIGHT = 1
