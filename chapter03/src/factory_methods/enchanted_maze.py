from src.door import Door
from src.enchanted import (
    EnchantedDoor,
    EnchantedRoom,
    EnchantedWall,
    Spell,
)
from src.factory_methods.maze_template import MazeTemplate
from src.maze import Maze
from src.room import Room
from src.wall import Wall


class EnchantedMazeGame(MazeTemplate):
    def make_maze(self) -> Maze:
        return Maze()

    def make_room(
        self,
        room_no: int,
    ) -> Room:
        return EnchantedRoom(room_no, self.cast_spell())

    def make_door(
        self,
        room1: Room,
        room2: Room,
    ) -> Door:
        return EnchantedDoor(room1, room2)

    def make_wall(self) -> Wall:
        return EnchantedWall()

    def cast_spell(self) -> Spell:
        return Spell(power=10)
