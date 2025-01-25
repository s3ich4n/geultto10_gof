from map_site import MapSite


class Door(MapSite):
    def __init__(self, room1=None, room2=None):
        self._room1 = room1
        self._room2 = room2
        self._is_open = False
    
    def enter(self):
        pass  # 문의 상태에 따른 진입 로직 구현
    
    def other_side_from(self, room):
        return self._room2 if room is self._room1 else self._room1
