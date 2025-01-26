from src.room import Room
from .wall import BombedWall


class RoomWithBomb(Room):
    def __init__(self, room_no):
        super().__init__(room_no)
        self._has_bomb = False
        self._bomb_exploded = False
    
    def enter(self):
        if self._damaged:
            # 손상된 벽은 통과 가능
            return True
        else:
            # 손상되지 않은 벽은 통과 불가
            return False

    def set_bomb(self, has_bomb: bool):
        self._has_bomb = has_bomb
    
    def has_bomb(self) -> bool:
        return self._has_bomb
    
    def explode(self):
        if self._has_bomb and not self._bomb_exploded:
            self._bomb_exploded = True
            # Damage all surrounding walls
            for side in self._sides:
                if isinstance(side, BombedWall):
                    side.damaged = True
