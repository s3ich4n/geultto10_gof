import pytest

from chapter04.decorator.src.components import (
    SimpleTextComponent,
)
from chapter04.decorator.src.decorators import (
    ItalicDecorator,
    BoldDecorator,
)


@pytest.fixture
def text():
    return SimpleTextComponent("Hello, Decorator Pattern!")


def test_component_runs():
    string = "Hello, Decorator Pattern!"
    sut = SimpleTextComponent(string)

    assert sut.get_text() == string


def test_italic_decorator_runs(text):
    # 이탤릭 데코레이터 적용
    sut = ItalicDecorator(text)

    assert sut.get_text() == "<i>Hello, Decorator Pattern!</i>"


def test_bold_decorator_runs(text):
    # 볼드 데코레이터 적용
    text = BoldDecorator(text)

    assert text.get_text() == "<b>Hello, Decorator Pattern!</b>"


def test_multi_decorator_runs(text):
    # Bold가 안에, italic이 밖에
    text = BoldDecorator(text)
    sut = ItalicDecorator(text)

    assert sut.get_text() == "<i><b>Hello, Decorator Pattern!</b></i>"
