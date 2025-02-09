from src.bombed import (
    BombedWall,
    RoomWithBomb,
)
from src.door import Door
from src.maze import Maze

from .maze_prototype import MazePrototypeFactory

bombed_prototype_factory = MazePrototypeFactory(
    Maze(),
    BombedWall(),
    RoomWithBomb(0),
    Door(None, None),
)
