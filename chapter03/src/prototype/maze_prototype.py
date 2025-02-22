from src.door import Door
from src.maze import Maze
from src.room import Room
from src.wall import Wall


class MazePrototypeFactory:
    def __init__(
        self,
        prototype_maze: Maze,
        prototype_wall: Wall,
        prototype_room: Room,
        prototype_door: Door,
    ):
        self._prototype_maze = prototype_maze
        self._prototype_wall = prototype_wall
        self._prototype_room = prototype_room
        self._prototype_door = prototype_door

    def make_maze(self) -> Maze:
        return self._prototype_maze.clone()

    def make_wall(self) -> Wall:
        return self._prototype_wall.clone()

    def make_room(self, room_no: int) -> Room:
        room = self._prototype_room.clone()
        room._room_number = room_no  # 복제 후 방 번호 설정
        return room

    def make_door(
        self,
        room1: Room,
        room2: Room,
    ) -> Door:
        door = self._prototype_door.clone()
        door._room1 = room1  # 복제 후 방 참조 설정
        door._room2 = room2
        return door
