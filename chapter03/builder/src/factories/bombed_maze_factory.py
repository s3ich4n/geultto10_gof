from src.factories.maze_factory import MazeFactory
from src.bombed.room import RoomWithBomb
from src.bombed.wall import BombedWall
from src.maze import Maze
from src.door import Door
from src.room import Room


class BombedMazeFactory(MazeFactory):
    def make_maze(self) -> Maze:
        return Maze()
    
    def make_wall(self) -> BombedWall:
        return BombedWall()
    
    def make_room(self, room_no: int) -> RoomWithBomb:
        return RoomWithBomb(room_no)
    
    def make_door(self, room1: Room, room2: Room) -> Door:
        return Door(room1, room2)
