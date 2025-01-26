from src.builder import (
    CountingMazeBuilder,
    StandardMazeBuilder,
)


def test_builder_encapsulation(maze_game):
    # 동일한 생성 프로세스로 다른 결과물
    standard_builder = StandardMazeBuilder()
    counting_builder = CountingMazeBuilder()
    
    # 동일한 생성 프로세스 사용
    maze_game.create_maze_with_builder(standard_builder)
    maze_game.create_maze_with_builder(counting_builder)
    
    # 다른 결과물 검증
    assert standard_builder.get_maze() is not None
    rooms, doors = counting_builder.get_counts()
    assert isinstance(rooms, int)
    assert isinstance(doors, int)

def test_builder_construction_steps(maze_game):
    builder = StandardMazeBuilder()
    
    # 단계별 생성 검증
    builder.build_maze()
    builder.build_room(1)
    maze = builder.get_maze()
    
    assert maze.room_no(1) is not None
    assert maze.room_no(2) is None  # 아직 생성되지 않음
