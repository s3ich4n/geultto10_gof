from src.door import Door
from src.factory_methods.maze_template import MazeTemplate
from src.maze import Maze
from src.room import Room
from src.wall import Wall


class NormalMazeGame(MazeTemplate):
    def make_maze(self) -> Maze:
        return Maze()

    def make_room(self, room_no: int) -> Room:
        return Room(room_no)

    def make_door(self, room1: Room, room2: Room) -> Door:
        return Door(room1, room2)

    def make_wall(self) -> Wall:
        return Wall()
