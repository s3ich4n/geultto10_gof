from map_site import MapSite
from enums import Direction


class Room(MapSite):
    def __init__(self, room_no):
        self._sides = [None] * 4  # 4면을 저장할 리스트
        self._room_number = room_no
    
    def get_side(self, direction: Direction):
        return self._sides[direction.value]
    
    def set_side(self, direction: Direction, map_site: MapSite):
        self._sides[direction.value] = map_site
    
    def enter(self):
        pass  # 실제 구현은 게임 로직에 따라 정의
