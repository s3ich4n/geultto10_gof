from src.door import Door
from src.maze import Maze
from src.room import Room
from src.wall import Wall

from .maze_prototype import MazePrototypeFactory

# 일반 미로용 프로토타입 팩토리
normal_prototype_factory = MazePrototypeFactory(
    Maze(),
    Wall(),
    Room(0),
    Door(None, None),
)
