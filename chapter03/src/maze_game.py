from src.builder.base import MazeBuilder
from src.factories.maze_factory import MazeFactory

from src.maze import Maze
from src.room import Room
from src.door import Door
from src.wall import Wall
from src.enums import Direction


class MazeGame:
    def create_maze(self, factory: MazeBuilder):
        a_maze = factory.make_maze()
        r1: Room = factory.make_room(1)
        r2: Room = factory.make_room(2)
        the_door: Door = factory.make_door(r1, r2)

        a_maze.add_room(r1)
        a_maze.add_room(r2)

        r1.set_side(Direction.NORTH, factory.make_wall())
        r1.set_side(Direction.EAST, the_door)
        r1.set_side(Direction.SOUTH, factory.make_wall())
        r1.set_side(Direction.WEST, factory.make_wall())
            
        r2.set_side(Direction.NORTH, factory.make_wall())
        r2.set_side(Direction.EAST, factory.make_wall())
        r2.set_side(Direction.SOUTH, factory.make_wall())
        r2.set_side(Direction.WEST, the_door)

        return a_maze

    def create_maze_with_builder(self, builder: MazeBuilder):
        builder.build_maze()
        builder.build_room(1)
        builder.build_room(2)
        builder.build_door(1, 2)
        return builder.get_maze()
