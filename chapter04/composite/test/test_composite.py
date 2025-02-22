from src.client import ImageEditor
from src.composite import CompoundGraphic
from src.leaves import (
    Dot,
    Circle,
)


def test_dot_operations():
    dot = Dot(5, 5)
    assert dot.draw() == "dot at (5, 5)"
    dot.move(2, 3)
    assert dot.get_position() == (7, 8)


def test_circle_operations():
    circle = Circle(10, 10, 5)
    assert circle.draw() == "circle at (10, 10) with radius 5"
    circle.move(-3, 2)
    assert circle.get_position() == (7, 12)


def test_compound_graphic_operations():
    compound = CompoundGraphic()
    dot = Dot(1, 1)
    circle = Circle(2, 2, 3)

    compound.add(dot)
    compound.add(circle)

    assert "dot at (1, 1)" in compound.draw()
    assert "circle at (2, 2)" in compound.draw()

    compound.move(1, 1)
    assert compound.get_position() == (2, 2)


def test_nested_compound_graphics():
    inner_compound = CompoundGraphic([Dot(0, 0), Circle(1, 1, 2)])
    outer_compound = CompoundGraphic([inner_compound, Dot(2, 2)])

    outer_compound.move(1, 1)
    assert "dot at (1, 1)" in inner_compound.draw()
    assert "circle at (2, 2)" in inner_compound.draw()
    assert "dot at (3, 3)" in outer_compound.draw()


def test_image_editor():
    editor = ImageEditor()
    editor.load()

    initial_graphics = editor.get_graphics()
    assert "dot at (1, 2)" in initial_graphics.draw()
    assert "circle at (5, 3)" in initial_graphics.draw()

    dot1 = Dot(0, 0)
    dot2 = Dot(1, 1)
    editor._all_graphics.add(dot1)
    editor._all_graphics.add(dot2)

    group = editor.group_selected([dot1, dot2])
    assert "dot at (0, 0)" in group.draw()
    assert "dot at (1, 1)" in group.draw()
