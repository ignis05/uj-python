from rectangles import Rectangle
from points import Point


def test_from_points():
    rectangle = Rectangle.from_points((Point(1, 1), Point(2, 3)))
    assert str(rectangle) == '[(1, 1), (2, 3)]'


def test_coords_getters():
    rect = Rectangle(0, 1, 3, 4)

    assert rect.top == 4
    assert rect.bottom == 1

    assert rect.left == 0
    assert rect.right == 3

    assert rect.height == 3
    assert rect.width == 3


def test_point_getters():
    p1 = Point(0, 1)
    p2 = Point(3, 4)
    rect = Rectangle.from_points((p1, p2))

    assert rect.bottomleft == p1
    assert rect.topright == p2
    assert rect.topleft == Point(p1.x, p2.y)
    assert rect.bottomright == Point(p2.x, p1.y)


def test_center():
    assert Rectangle(0, 1, 3, 4).center == Point(1.5, 2.5)
