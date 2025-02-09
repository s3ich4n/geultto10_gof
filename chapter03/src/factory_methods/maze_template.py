from abc import (
    ABC,
    abstractmethod,
)

from src.door import Door
from src.enums import Direction
from src.maze import Maze
from src.room import Room
from src.wall import Wall


class MazeTemplate(ABC):
    # 템플릿 메서드: 미로 생성 알고리즘의 뼈대를 정의
    def create_maze(self) -> Maze:
        # 미로 생성
        maze = self.make_maze()

        # 방 생성
        r1 = self.make_room(1)
        r2 = self.make_room(2)

        # 문 생성
        door = self.make_door(r1, r2)

        # 미로에 방 추가
        maze.add_room(r1)
        maze.add_room(r2)

        # 방 구조 설정
        self.initialize_room(r1, door, Direction.EAST)
        self.initialize_room(r2, door, Direction.WEST)

        return maze

    # Factory Methods
    @abstractmethod
    def make_maze(self) -> Maze:
        pass

    @abstractmethod
    def make_room(
        self,
        room_no: int,
    ) -> Room:
        pass

    @abstractmethod
    def make_door(
        self,
        room1: Room,
        room2: Room,
    ) -> Door:
        pass

    @abstractmethod
    def make_wall(self) -> Wall:
        pass

    # Helper 메서드
    def initialize_room(
        self,
        room: Room,
        door: Door,
        door_direction: Direction,
    ):
        room.set_side(Direction.NORTH, self.make_wall())
        room.set_side(Direction.SOUTH, self.make_wall())
        room.set_side(Direction.EAST, self.make_wall())
        room.set_side(Direction.WEST, self.make_wall())
        room.set_side(door_direction, door)
