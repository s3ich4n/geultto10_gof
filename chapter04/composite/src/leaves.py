from src.graphic import Graphic


class Dot(Graphic):
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def move(self, x: int, y: int):
        self._x += x
        self._y += y

    def draw(self) -> str:
        return f"dot at ({self._x}, {self._y})"

    def get_position(self) -> tuple[int, int]:
        return self._x, self._y


class Circle(Graphic):
    def __init__(self, x: int, y: int, radius: float):
        self._x = x
        self._y = y
        self._radius = radius

    def move(self, x: int, y: int):
        self._x += x
        self._y += y

    def draw(self) -> str:
        return f"circle at ({self._x}, {self._y}) with radius {self._radius}"

    def get_position(self) -> tuple[int, int]:
        return self._x, self._y
