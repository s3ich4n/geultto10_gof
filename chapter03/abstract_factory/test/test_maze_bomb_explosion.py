from src.enums import Direction


def test_bomb_explosion(bombed_maze):
    room1 = bombed_maze.room_no(1)
    
    # Set bomb in room1
    room1.set_bomb(True)
    assert room1.has_bomb()
    
    # Get surrounding walls before explosion
    north_wall = room1.get_side(Direction.NORTH)
    west_wall = room1.get_side(Direction.WEST)
    
    # Verify walls are not damaged initially
    assert not north_wall.damaged
    assert not west_wall.damaged
    
    # Trigger explosion
    room1.explode()
    
    # Verify walls are damaged after explosion
    assert north_wall.damaged
    assert west_wall.damaged
