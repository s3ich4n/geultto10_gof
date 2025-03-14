from src.graphic import Graphic


class CompoundGraphic(Graphic):
    def __init__(self, graphics: list[Graphic] = None):
        self._graphics = graphics if graphics is not None else []

    def add(self, child: Graphic) -> None:
        self._graphics.append(child)

    def remove(self, child: Graphic) -> None:
        self._graphics.remove(child)  # 실제 객체 비교로 변경

    def move(self, x: int, y: int) -> None:
        for graphic in self._graphics:
            graphic.move(x, y)

    def draw(self) -> str:
        if not self._graphics:
            return "empty compound"
        results = []
        for graphic in self._graphics:
            results.append(graphic.draw())
        return f"compound: {', '.join(results)}"

    def get_position(self) -> tuple[int, int]:
        if not self._graphics:
            return 0, 0
        # 모든 그래픽의 중심점 평균을 반환
        x_sum = sum(g.get_position()[0] for g in self._graphics)
        y_sum = sum(g.get_position()[1] for g in self._graphics)
        return x_sum // len(self._graphics), y_sum // len(self._graphics)
