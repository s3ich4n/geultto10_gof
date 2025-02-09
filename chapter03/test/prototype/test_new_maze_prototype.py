from src.bombed import (
    RoomWithBomb,
    BombedWall,
)
from src.door import Door
from src.enchanted import (
    EnchantedWall,
    EnchantedDoor,
    EnchantedRoom,
)
from src.enums import Direction
from src.room import Room
from src.wall import Wall


#
# 주요 이점:
#   복잡한 초기화 로직을 한 곳에 모아둘 수 있음
#   이미 만들어진 객체를 복제하므로 객체 생성 비용 절감
#   런타임에 객체의 종류를 쉽게 전환할 수 있음
#


def test_create_normal_maze_prototype(normal_maze_prototype):
    # Then
    # 1. 미로에 두 개의 방이 있는지 확인
    assert normal_maze_prototype.room_no(1) is not None
    assert normal_maze_prototype.room_no(2) is not None

    # 2. 각 방의 구조 확인
    room1 = normal_maze_prototype.room_no(1)
    room2 = normal_maze_prototype.room_no(2)

    # Room 1 검증
    assert isinstance(room1, Room)
    assert isinstance(room1.get_side(Direction.NORTH), Wall)
    assert isinstance(room1.get_side(Direction.EAST), Door)
    assert isinstance(room1.get_side(Direction.SOUTH), Wall)
    assert isinstance(room1.get_side(Direction.WEST), Wall)

    # Room 2 검증
    assert isinstance(room2, Room)
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


def test_create_ehchanted_maze_prototype(enchanted_maze_prototype):
    # 1. 미로에 두 개의 방이 있는지 확인
    assert enchanted_maze_prototype.room_no(1) is not None
    assert enchanted_maze_prototype.room_no(2) is not None

    # 2. 각 방의 구조 확인
    room1 = enchanted_maze_prototype.room_no(1)
    room2 = enchanted_maze_prototype.room_no(2)

    # Room 1 검증
    assert isinstance(room1, EnchantedRoom)
    assert hasattr(room1, "spell")
    assert room1.spell.power > 0
    assert isinstance(room1.get_side(Direction.NORTH), EnchantedWall)
    assert isinstance(room1.get_side(Direction.EAST), EnchantedDoor)
    assert isinstance(room1.get_side(Direction.SOUTH), EnchantedWall)
    assert isinstance(room1.get_side(Direction.WEST), EnchantedWall)

    # Room 2 검증
    assert isinstance(room2, EnchantedRoom)
    assert hasattr(room2, "spell")
    assert room2.spell.power > 0
    assert isinstance(room2.get_side(Direction.NORTH), EnchantedWall)
    assert isinstance(room2.get_side(Direction.EAST), EnchantedWall)
    assert isinstance(room2.get_side(Direction.SOUTH), EnchantedWall)
    assert isinstance(room2.get_side(Direction.WEST), EnchantedDoor)

    # 3. 문이 두 방을 올바르게 연결하는지 확인
    door1 = room1.get_side(Direction.EAST)
    door2 = room2.get_side(Direction.WEST)

    assert door1 is door2  # 같은 문 객체를 참조하는지 확인
    assert door1.other_side_from(room1) is room2
    assert door2.other_side_from(room2) is room1


def test_create_bombed_maze_prototype(bombed_maze_prototype):
    # Verify rooms are created as RoomWithBomb
    room1 = bombed_maze_prototype.room_no(1)
    room2 = bombed_maze_prototype.room_no(2)

    assert isinstance(room1, RoomWithBomb)
    assert isinstance(room2, RoomWithBomb)

    # Verify walls are created as BombedWall
    north_wall = room1.get_side(Direction.NORTH)
    assert isinstance(north_wall, BombedWall)
