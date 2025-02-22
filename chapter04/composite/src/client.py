from src.composite import CompoundGraphic
from src.graphic import Graphic
from src.leaves import (
    Dot,
    Circle,
)


class ImageEditor:
    def __init__(self):
        self._all_graphics = CompoundGraphic()

    def load(self) -> None:
        self._all_graphics = CompoundGraphic(
            [
                Dot(1, 2),
                Circle(5, 3, 10),
            ]
        )

    def group_selected(self, components: list[Graphic]) -> CompoundGraphic:
        group = CompoundGraphic(components)
        # 기존 그래픽에서 선택된 컴포넌트들을 제거
        for component in components:
            if component in self._all_graphics._graphics:
                self._all_graphics.remove(component)
        # 새로운 그룹을 추가
        self._all_graphics.add(group)
        return group

    def get_graphics(self) -> CompoundGraphic:
        return self._all_graphics
