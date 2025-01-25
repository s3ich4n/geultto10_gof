import pytest

from src.maze_game import MazeGame
from src.factories.enchanted_maze_factory import EnchantedMazeFactory
from src.factories.normal_maze_factory import NormalMazeFactory


@pytest.fixture
def maze_game():
    return MazeGame()


@pytest.fixture
def normal_maze(maze_game):
    return maze_game.create_maze(NormalMazeFactory())


@pytest.fixture
def enchanted_maze(maze_game):
    return maze_game.create_maze(EnchantedMazeFactory())
