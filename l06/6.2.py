import unittest


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return f'({self.x}, {self.y})'

    def __repr__(self):        # zwraca string "Point(x, y)"
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):   # obsługa point1 == point2
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return (self.x ** 2 + self.y**2)**(1/2)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.


class TestPoint(unittest.TestCase):
    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(Point(0, 0)), '(0, 0)')
        self.assertEqual(str(Point(10, 0)), '(10, 0)')
        self.assertEqual(str(Point(52342, 12389123)), '(52342, 12389123)')

    def test_repr(self):
        self.assertEqual(repr(Point(0, 0)), 'Point(0, 0)')
        self.assertEqual(repr(Point(10, 0)), 'Point(10, 0)')
        self.assertEqual(repr(Point(52342, 12389123)), 'Point(52342, 12389123)')

    def test_eq_and_ne(self):
        self.assertEqual(Point(0, 0), Point(0, 0))
        self.assertNotEqual(Point(0, 0), Point(5, 5))
        self.assertNotEqual(Point(5, 5), '(5, 5)')
        self.assertNotEqual(Point(5, 5), 'Point(5, 5)')

    def test_add(self):
        self.assertEqual(Point(1, 1)+Point(2, 3), Point(3, 4))
        self.assertEqual(Point(1, 2)+Point(-10, -11), Point(-9, -9))

    def test_sub(self):
        self.assertEqual(Point(1, 1)-Point(2, 3), Point(-1, -2))
        self.assertEqual(Point(1, 2)-Point(-10, -11), Point(11, 13))

    def test_mul(self):
        self.assertEqual(Point(1, 1)*Point(2, 3), 5)
        self.assertEqual(Point(1, 2)*Point(-10, -11), -32)

    def test_cross(self):
        self.assertEqual(Point(1, 1).cross(Point(2, 3)), 1)
        self.assertEqual(Point(1, 2).cross(Point(-10, -11)), 9)

    def test_length(self):
        self.assertEqual(Point(1, 1).length(), 2**(1/2))
        self.assertEqual(Point(5, 8).length(), 89**(1/2))

    def test_hash(self):
        self.assertEqual(hash(Point(1, 1)), 8389048192121911274)
        self.assertEqual(hash(Point(15, 8)), -8694819105557784667)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
