from src.enchanted import (
    EnchantedRoom,
    EnchantedWall,
    EnchantedDoor,
    Spell,
)
from src.maze import Maze

from .maze_prototype import MazePrototypeFactory

# 마법 미로용 프로토타입 팩토리
enchanted_prototype_factory = MazePrototypeFactory(
    Maze(),
    EnchantedWall(),
    EnchantedRoom(0, Spell(power=10)),
    EnchantedDoor(None, None),
)
