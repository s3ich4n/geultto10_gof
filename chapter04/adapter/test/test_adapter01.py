import pytest

from src.adapter import SquarePegAdapter
from src.round_hole import RoundHole
from src.round_peg import RoundPeg
from src.square_peg import SquarePeg


@pytest.fixture
def hole():
    return RoundHole(5)


def test_round_hole_and_round_peg():
    """둥근 구멍과 둥근 말뚝이 잘 맞는지 확인하는 테스트"""
    hole = RoundHole(5)
    peg = RoundPeg(5)
    assert hole.fits(peg) is True


def test_round_hole_and_square_peg_no_adapter(hole):
    """둥근 구멍과 네모 말뚝이 맞지 않는지 확인하는 테스트"""
    small_sqpeg = SquarePeg(5)

    # incompatible interface
    with pytest.raises(AttributeError):
        hole.fits(small_sqpeg)


def test_round_hole_and_square_peg_with_adapter(hole):
    """둥근 구멍과 네모 말뚝이 잘 맞는지 확인하는 테스트"""

    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)
    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)

    assert hole.fits(small_sqpeg_adapter) is True
    assert hole.fits(large_sqpeg_adapter) is False
