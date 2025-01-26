from src.maze import Maze
from src.enchanted import (
    EnchantedDoor,
    EnchantedRoom,
    EnchantedWall,
    Spell,
)
from src.factories.maze_factory import MazeFactory


class EnchantedMazeFactory(MazeFactory):
    def make_maze(self) -> Maze:
        return Maze()

    def make_wall(self):
        return EnchantedWall()
    
    def make_room(self, room_no: int) -> EnchantedRoom:
        return EnchantedRoom(room_no, self.cast_spell())

    def make_door(self, room_from, room_to) -> EnchantedDoor:
        return EnchantedDoor(room_from, room_to)

    def cast_spell(self) -> Spell:
        return Spell(power=10)
