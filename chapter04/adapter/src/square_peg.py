class SquarePeg:
    """네모 모양의 말뚝"""

    def __init__(self, width):
        """

        Args:
            width: 말뚝 너비
        """
        self._width = width

    @property
    def width(self):
        return self._width
