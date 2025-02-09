from copy import deepcopy

from src.map_site import MapSite


class Wall(MapSite):
    def enter(self):
        pass  # "벽에 부딪힘" 로직 구현

    def clone(self):
        return deepcopy(self)  # deep copy vs shallow copy
