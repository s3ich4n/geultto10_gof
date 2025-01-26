from src.maze import Maze
from src.room import Room
from src.door import Door
from src.wall import Wall
from src.enums import Direction

from .base import MazeBuilder


class CountingMazeBuilder(MazeBuilder):
    def __init__(self):
        self._rooms = 0
        self._doors = 0
    
    def build_room(self, room_no):
        self._rooms += 1
    
    def build_door(self, room_from, room_to):
        self._doors += 1

    def get_counts(self):
        return self._rooms, self._doors
