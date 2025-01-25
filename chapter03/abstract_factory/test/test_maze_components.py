from src.door import Door
from src.enums import Direction
from src.room import Room
from src.wall import Wall


class TestMazeComponents:
    def test_room_initialization(self):
        room = Room(1)
        assert room._room_number == 1
        assert len(room._sides) == 4
        assert all(side is None for side in room._sides)
    
    def test_room_side_setting(self):
        room = Room(1)
        wall = Wall()
        room.set_side(Direction.NORTH, wall)
        assert room.get_side(Direction.NORTH) == wall
    
    def test_door_connection(self):
        room1 = Room(1)
        room2 = Room(2)
        door = Door(room1, room2)
        assert door._room1 == room1
        assert door._room2 == room2
        assert door._is_open == False
        assert door.other_side_from(room1) == room2
        assert door.other_side_from(room2) == room1
