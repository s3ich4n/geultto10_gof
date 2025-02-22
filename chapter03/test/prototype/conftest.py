import pytest

from src.prototype import (
    bombed_prototype_factory,
    enchanted_prototype_factory,
    normal_prototype_factory,
)


@pytest.fixture
def normal_maze_prototype(maze_game):
    return maze_game.create_maze_with_pure_prototype(normal_prototype_factory)


@pytest.fixture
def enchanted_maze_prototype(maze_game):
    # 마법 미로용 프로토타입 팩토리
    return maze_game.create_maze_with_pure_prototype(enchanted_prototype_factory)


@pytest.fixture
def bombed_maze_prototype(maze_game):
    # 폭탄 미로용 프로토타입 팩토리
    return maze_game.create_maze_with_pure_prototype(bombed_prototype_factory)
