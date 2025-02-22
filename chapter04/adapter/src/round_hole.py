class RoundHole:
    """원형 구멍을 표현하는 클래스"""

    def __init__(self, radius):
        """

        Args:
            radius: 원형 구멍의 반지름
        """
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def fits(self, peg):
        """이 구멍에 말뚝이 들어맞는지 판단

        Args:
            peg: 말뚝의 반지름

        Returns:

        """
        return self.radius >= peg.radius
