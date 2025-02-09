from enum import (
    Enum,
    StrEnum,
)


class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3


class MazePrototype(StrEnum):
    NORMAL = "normal"
    ENCHANTED = "enchanted"
    BOMBED = "bombed"
