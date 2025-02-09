from copy import deepcopy

from src.map_site import MapSite
from src.enums import Direction


class Room(MapSite):
    def __init__(self, room_no):
        self._sides = [None] * 4  # 4면을 저장할 리스트
        self._room_number = room_no

    def clone(self):
        return deepcopy(self)   # deep copy vs shallow copy

    def get_side(self, direction: Direction):
        return self._sides[direction.value]
    
    def set_side(self, direction: Direction, map_site: MapSite):
        self._sides[direction.value] = map_site
    
    def enter(self):
        pass  # 실제 구현은 게임 로직에 따라 정의
