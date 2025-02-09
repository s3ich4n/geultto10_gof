from src.bombed import (
    BombedWall,
    RoomWithBomb,
)
from src.door import Door
from src.factory_methods.maze_template import MazeTemplate
from src.maze import Maze
from src.room import Room


class BombedMazeGame(MazeTemplate):
    def make_maze(self) -> Maze:
        # 미로 생성
        return Maze()

    def make_door(
        self,
        room1: Room,
        room2: Room,
    ) -> Door:
        return Door(room1, room2)

    def make_wall(self) -> BombedWall:
        return BombedWall()

    def make_room(
        self,
        room_no: int,
    ) -> RoomWithBomb:
        return RoomWithBomb(room_no)
