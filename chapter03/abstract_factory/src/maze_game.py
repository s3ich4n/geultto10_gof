from maze import Maze
from room import Room
from door import Door
from wall import Wall
from enums import Direction


class MazeGame:
    def create_maze(self):
        a_maze = Maze()     # concrete class 가 하드코딩 되어있음
        r1 = Room(1)        # 자연스럽게 변화에 취약해짐
        r2 = Room(2)
        the_door = Door(r1, r2)
        
        a_maze.add_room(r1)
        a_maze.add_room(r2)
        
        r1.set_side(Direction.NORTH, Wall())
        r1.set_side(Direction.EAST, the_door)
        r1.set_side(Direction.SOUTH, Wall())
        r1.set_side(Direction.WEST, Wall())
        
        r2.set_side(Direction.NORTH, Wall())
        r2.set_side(Direction.EAST, Wall())
        r2.set_side(Direction.SOUTH, Wall())
        r2.set_side(Direction.WEST, the_door)
        
        return a_maze
