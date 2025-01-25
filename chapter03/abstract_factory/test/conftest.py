from src.maze_game import MazeGame
import pytest

# Fixtures
@pytest.fixture
def maze_game():
    return MazeGame()

@pytest.fixture
def basic_maze(maze_game):
    return maze_game.create_maze()
