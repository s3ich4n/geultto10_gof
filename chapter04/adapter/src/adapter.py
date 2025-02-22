import math

from src.square_peg import SquarePeg


class SquarePegAdapter:
    """네모 말뚝을 둥근 구멍에 맞추기 위한 어댑터 클래스"""

    def __init__(self, peg: SquarePeg):
        self.peg = peg

    @property
    def radius(self):
        """네모 말뚝의 대각선 길이를 구하는 메서드

        Notes:
            네모 말뚝의 한 변의 길이가 `width`인 경우, 대각선 길이는 `width * sqrt(2)`
            이때, 원의 반지름은 대각선의 절반이므로 계산식은 `width * sqrt(2) / 2`가 되어,
            둥근 구멍에 맞는 유효 반지름으로 사용할 수 있다.

        Returns:

        """
        return self.peg.width * math.sqrt(2) / 2
