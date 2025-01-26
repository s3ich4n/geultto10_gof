import pytest

from src.maze_game import MazeGame
from src.factories import (
    EnchantedMazeFactory,
    BombedMazeFactory,
    NormalMazeFactory,
)
from src.builder import (
    CountingMazeBuilder,
    StandardMazeBuilder,
)


@pytest.fixture
def maze_game():
    return MazeGame()


@pytest.fixture
def normal_maze(maze_game):
    return maze_game.create_maze(NormalMazeFactory())


@pytest.fixture
def enchanted_maze(maze_game):
    return maze_game.create_maze(EnchantedMazeFactory())


@pytest.fixture
def bombed_maze(maze_game):
    return maze_game.create_maze(BombedMazeFactory())


@pytest.fixture
def mage_built_by_standard(maze_game):
    return maze_game.create_maze_with_builder(StandardMazeBuilder())


@pytest.fixture
def maze_built_by_continuing(maze_game):
    builder = CountingMazeBuilder()
    maze_game.create_maze_with_builder(builder)
    return builder
