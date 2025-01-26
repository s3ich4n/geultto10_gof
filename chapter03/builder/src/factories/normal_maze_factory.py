from src.maze import Maze
from src.room import Room
from src.door import Door
from src.wall import Wall
from src.factories.maze_factory import MazeFactory


class NormalMazeFactory(MazeFactory):
    def make_maze(self) -> Maze:
        return Maze()
    
    def make_wall(self) -> Wall:
        return Wall()
    
    def make_room(self, room_no: int) -> Room:
        return Room(room_no)
    
    def make_door(self, room1: Room, room2: Room) -> Door:
        return Door(room1, room2)
