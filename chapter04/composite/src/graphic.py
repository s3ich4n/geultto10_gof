from abc import (
    ABC,
    abstractmethod,
)


class Graphic(ABC):
    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass

    @abstractmethod
    def draw(self) -> str:
        pass

    @abstractmethod
    def get_position(self) -> tuple[int, int]:
        pass
