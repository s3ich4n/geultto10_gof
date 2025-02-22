from copy import deepcopy

from src.map_site import MapSite


class Door(MapSite):
    def __init__(self, room1=None, room2=None):
        self._room1 = room1
        self._room2 = room2
        self._is_open = False

    def clone(self):
        # door = deepcopy(self)     # shallow copy - 복제 시 room 참조를 초기화
        # door._room1 = None
        # door._room2 = None
        # return door
        return deepcopy(self)   # deep copy - 전체 값을 복사

    def enter(self):
        pass  # 문의 상태에 따른 진입 로직 구현
    
    def other_side_from(self, room):
        return self._room2 if room is self._room1 else self._room1
