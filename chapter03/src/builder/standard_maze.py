from src.maze import Maze
from src.room import Room
from src.door import Door
from src.wall import Wall
from src.enums import Direction

from .base import MazeBuilder


class StandardMazeBuilder(MazeBuilder):
    def __init__(self):
        self._current_maze = None
    
    def build_maze(self):
        self._current_maze = Maze()
    
    def build_room(self, room_no):
        if not self._current_maze.room_no(room_no):
            room = Room(room_no)
            self._current_maze.add_room(room)
            room.set_side(Direction.NORTH, Wall())
            room.set_side(Direction.SOUTH, Wall())
            room.set_side(Direction.EAST, Wall())
            room.set_side(Direction.WEST, Wall())
    
    def build_door(self, room_from, room_to):
        r1 = self._current_maze.room_no(room_from)
        r2 = self._current_maze.room_no(room_to)
        d = Door(r1, r2)
        
        # TODO - 공통 벽 방향 찾기 로직 필요
        direction = self._common_wall(r1, r2)
        r1.set_side(direction, d)
        r2.set_side(self._opposite_direction(direction), d)
    
    def get_maze(self):
        return self._current_maze
    
    def _common_wall(self, room1, room2):
        # 간단한 구현: 인접한 방은 동-서 또는 남-북으로 연결
        # 실제로는 더 복잡한 로직이 필요할 수 있음
        return Direction.EAST
    
    def _opposite_direction(self, direction):
        if direction == Direction.NORTH: return Direction.SOUTH
        if direction == Direction.SOUTH: return Direction.NORTH
        if direction == Direction.EAST: return Direction.WEST
        if direction == Direction.WEST: return Direction.EAST
