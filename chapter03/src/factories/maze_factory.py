from abc import ABC, abstractmethod

from src.maze import Maze
from src.room import Room
from src.door import Door
from src.wall import Wall


class MazeFactory(ABC):
    @abstractmethod
    def make_maze(self) -> Maze:
        pass
    
    @abstractmethod
    def make_wall(self) -> Wall:
        pass
    
    @abstractmethod
    def make_room(self) -> Room:
        pass
    
    @abstractmethod
    def make_door(self, room_from, room_to) -> Door:
        pass
