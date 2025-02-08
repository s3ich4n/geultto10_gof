import pytest
from src.bombed import (
    RoomWithBomb,
    BombedWall,
)
from src.door import Door
from src.enchanted import (
    EnchantedRoom,
    EnchantedWall,
    EnchantedDoor,
)
from src.enums import Direction
from src.factory_methods import (
    NormalMazeGame,
    EnchantedMazeGame,
    BombedMazeGame,
)
from src.room import Room
from src.wall import Wall


@pytest.fixture
def normal_game():
    return NormalMazeGame()


@pytest.fixture
def enchanted_game():
    return EnchantedMazeGame()


@pytest.fixture
def bombed_game():
    return BombedMazeGame()


@pytest.fixture
def normal_maze(normal_game):
    return normal_game.create_maze()


@pytest.fixture
def enchanted_maze(enchanted_game):
    return enchanted_game.create_maze()


@pytest.fixture
def bombed_maze(bombed_game):
    return bombed_game.create_maze()


def test_create_normal_maze(normal_maze):
    # Then
    # 1. 미로에 두 개의 방이 있는지 확인
    assert normal_maze.room_no(1) is not None
    assert normal_maze.room_no(2) is not None

    # 2. 각 방의 구조 확인
    room1 = normal_maze.room_no(1)
    room2 = normal_maze.room_no(2)

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


def test_create_enchanted_maze(enchanted_maze):
    # 1. 미로에 두 개의 방이 있는지 확인
    assert enchanted_maze.room_no(1) is not None
    assert enchanted_maze.room_no(2) is not None

    # 2. 각 방의 구조 확인
    room1 = enchanted_maze.room_no(1)
    room2 = enchanted_maze.room_no(2)

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


def test_create_bombed_maze(bombed_maze):
    # RoomWithBomb, BombedWall을 제대로 갖고있나 확인
    room1 = bombed_maze.room_no(1)
    room2 = bombed_maze.room_no(2)

    assert isinstance(room1, RoomWithBomb)
    assert isinstance(room2, RoomWithBomb)

    # Verify walls are created as BombedWall
    north_wall = room1.get_side(Direction.NORTH)
    assert isinstance(north_wall, BombedWall)


def test_factory_methods_individually():
    # 각 Factory Method가 올바른 타입의 객체를 생성하는지 개별적으로 테스트
    normal_game = NormalMazeGame()
    enchanted_game = EnchantedMazeGame()
    bombed_game = BombedMazeGame()

    # Normal game factory methods
    assert isinstance(normal_game.make_wall(), Wall)
    assert isinstance(normal_game.make_room(1), Room)
    room1 = normal_game.make_room(1)
    room2 = normal_game.make_room(2)
    assert isinstance(normal_game.make_door(room1, room2), Door)

    # Enchanted game factory methods
    assert isinstance(enchanted_game.make_wall(), EnchantedWall)
    enchanted_room = enchanted_game.make_room(1)
    assert isinstance(enchanted_room, EnchantedRoom)
    assert hasattr(enchanted_room, "spell")

    # Bombed game factory methods
    assert isinstance(bombed_game.make_wall(), BombedWall)
    assert isinstance(bombed_game.make_room(1), RoomWithBomb)
