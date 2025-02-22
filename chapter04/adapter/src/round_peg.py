class RoundPeg:
    """원형 말뚝을 표현한 클래스"""

    def __init__(self, radius):
        """

        Args:
            radius: 말뚝의 반지름
        """
        self._radius = radius

    @property
    def radius(self):
        return self._radius
