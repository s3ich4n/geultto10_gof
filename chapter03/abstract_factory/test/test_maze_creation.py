import pytest
from maze_game import MazeGame
from room import Room
from door import Door
from wall import Wall
from enums import Direction


def test_create_maze():
    # Given
    game = MazeGame()
    
    # When
    maze = game.create_maze()
    
    # Then
    # 1. 미로에 두 개의 방이 있는지 확인
    assert maze.room_no(1) is not None
    assert maze.room_no(2) is not None
    
    # 2. 각 방의 구조 확인
    room1 = maze.room_no(1)
    room2 = maze.room_no(2)
    
    # Room 1 검증
    assert isinstance(room1.get_side(Direction.NORTH), Wall)
    assert isinstance(room1.get_side(Direction.EAST), Door)
    assert isinstance(room1.get_side(Direction.SOUTH), Wall)
    assert isinstance(room1.get_side(Direction.WEST), Wall)
    
    # Room 2 검증
    assert isinstance(room2.get_side(Direction.NORTH), Wall)
    assert isinstance(room2.get_side(Direction.EAST), Wall)
    assert isinstance(room2.get_side(Direction.SOUTH), Wall)
    assert isinstance(room2.get_side(Direction.WEST), Door)
    
    # 3. 문이 두 방을 올바르게 연결하는지 확인
    door1 = room1.get_side(Direction.EAST)
    door2 = room2.get_side(Direction.WEST)
    
    assert door1 is door2  # 같은 문 객체를 참조하는지 확인
    assert door1.other_side_from(room1) is room2
    assert door2.other_side_from(room2) is room1
