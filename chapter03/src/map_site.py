from abc import ABC, abstractmethod


# 미로 구성요소의 추상 기본 클래스
class MapSite(ABC):
    @abstractmethod
    def enter(self):
        pass
