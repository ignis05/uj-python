import unittest
from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Point 1 must have lower coordinates than Point 2")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
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

    def intersection(self, other):  # część wspólna prostokątów
        if not isinstance(other, Rectangle):
            raise ValueError("Other is not a rectangle")
        h_p1_X = max(self.pt1.x, other.pt1.x)
        h_p1_Y = max(self.pt1.y, other.pt1.y)
        l_p2_X = min(self.pt2.x, other.pt2.x)
        l_p2_Y = min(self.pt2.y, other.pt2.y)
        if h_p1_X >= l_p2_X or h_p1_Y >= l_p2_Y:
            raise ValueError("Rectangles have no intersection")
        return Rectangle(h_p1_X, h_p1_Y, l_p2_X, l_p2_Y)

    def cover(self, other):    # prostąkąt nakrywający oba
        if not isinstance(other, Rectangle):
            raise ValueError("Other is not a rectangle")
        lowestX = min(self.pt1.x, other.pt1.x)
        lowestY = min(self.pt1.y, other.pt1.y)
        heighestX = max(self.pt2.x, other.pt2.x)
        heighestY = max(self.pt2.y, other.pt2.y)
        return Rectangle(lowestX, lowestY, heighestX, heighestY)

    def make4(self):           # zwraca krotkę czterech mniejszych
        center = self.center()
        return (
            Rectangle(self.pt1.x, center.y, center.x, self.pt2.y),  # A
            Rectangle(center.x, center.y, self.pt2.x, self.pt2.y),  # B
            Rectangle(center.x, self.pt1.y, self.pt2.x, center.y),  # C
            Rectangle(self.pt1.x, self.pt1.y, center.x, center.y),  # D
        )
# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C


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

    def test_cover(self):
        r1 = Rectangle(1, 1, 3, 3)
        r2 = Rectangle(2, 2, 4, 4)
        self.assertEqual(r1.cover(r1), r1)
        self.assertEqual(r2.cover(r2), r2)
        self.assertEqual(r1.cover(r2), r2.cover(r1))
        r3 = r1.cover(r2)
        self.assertEqual(r3.cover(r1), r3)
        self.assertEqual(r3.cover(r2), r3)
        self.assertEqual(r3, Rectangle(1, 1, 4, 4))

    def test_intersection(self):
        r1 = Rectangle(1, 1, 3, 3)
        r2 = Rectangle(2, 2, 4, 4)
        self.assertEqual(r1.intersection(r2), r2.intersection(r1))
        r3 = r1.intersection(r2)
        self.assertEqual(r3, Rectangle(2, 2, 3, 3))
        self.assertEqual(r3, r3.intersection(r1))
        self.assertEqual(r3, r3.intersection(r2))

    def test_make4(self):
        r1, r2, r3, r4 = Rectangle(0, 0, 4, 4).make4()
        self.assertEqual(r1, Rectangle(0, 2, 2, 4))
        self.assertEqual(r2, Rectangle(2, 2, 4, 4))
        self.assertEqual(r3, Rectangle(2, 0, 4, 2))
        self.assertEqual(r4, Rectangle(0, 0, 2, 2))
        self.assertEqual(r1.area(), r2.area())
        self.assertEqual(r2.area(), r3.area())
        self.assertEqual(r3.area(), r4.area())


if __name__ == '__main__':
    unittest.main()
