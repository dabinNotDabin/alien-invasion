import enum


class Direction(enum.IntEnum):
    LEFT = -1
    RIGHT = 1

    @staticmethod
    def opposite(self):
        if self == Direction.LEFT:
            return Direction.RIGHT

        return Direction.LEFT
