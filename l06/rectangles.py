# W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami.
# Prostokąt jest określony przez podanie dwóch wierzchołków, lewego dolnego i prawego górnego.
# Napisać kod testujący moduł rectangles.

# ? założenia: wierzchołki są zawsze podawane w kolejności lower-left upper-right | move() jest operacją w miejscu, nie zwraca nic

import unittest
from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return f'[{self.pt1}, {self.pt2}]'

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

    def __eq__(self, other):   # obsługa rect1 == rect2
        return isinstance(other, Rectangle) and self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        pt3 = self.pt1 + self.pt2
        return Point(pt3.x/2, pt3.y/2)

    def area(self):            # pole powierzchni
        width = abs(self.pt2.x - self.pt1.x)
        height = abs(self.pt2.y - self.pt1.y)
        return width * height

    def move(self, x, y):      # przesunięcie o (x, y)
        pt3 = Point(x, y)
        self.pt1 += pt3
        self.pt2 += pt3


# Kod testujący moduł.
class TestRectangle(unittest.TestCase):
    def setUp(self): pass
    def tearDown(self): pass

    def test_str(self):
        self.assertEqual(str(Rectangle(1, 2, 3, 4)), '[(1, 2), (3, 4)]')
        self.assertEqual(str(Rectangle(5, 6, 7, 8)), '[(5, 6), (7, 8)]')

    def test_repr(self):
        self.assertEqual(repr(Rectangle(1, 2, 3, 4)), 'Rectangle(1, 2, 3, 4)')
        self.assertEqual(repr(Rectangle(5, 6, 7, 8)), 'Rectangle(5, 6, 7, 8)')

    def test_eg_and_ne(self):
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle(1, 2, 3, 4))
        self.assertEqual(Rectangle(5, 6, 7, 8), Rectangle(5, 6, 7, 8))
        self.assertNotEqual(Rectangle(1, 2, 3, 4), Rectangle(1, 2, 3, 8))
        self.assertNotEqual(Rectangle(5, 6, 7, 8), Rectangle(1, 6, 7, 8))

    def test_center(self):
        self.assertEqual(Rectangle(1, 1, 3, 3).center(), Point(2, 2))
        self.assertEqual(Rectangle(10, 20, 30, 40).center(), Point(20, 30))

    def test_area(self):
        self.assertEqual(Rectangle(1, 1, 3, 3).area(), 4)
        self.assertEqual(Rectangle(1, 1, 3, 3).area(), Rectangle(0, 0, 2, 2).area())
        self.assertEqual(Rectangle(1, 1, 3, 3).area(), Rectangle(-2, -2, 0, 0).area())
        self.assertEqual(Rectangle(0, 0, 10, 10).area(), 100)

    def test_move(self):
        r1 = Rectangle(1, 1, 3, 3)
        r1.move(-1, -1)
        self.assertEqual(r1, Rectangle(0, 0, 2, 2))
        r1.move(1, -1)
        self.assertEqual(r1, Rectangle(1, -1, 3, 1))


if __name__ == '__main__':
    unittest.main()
