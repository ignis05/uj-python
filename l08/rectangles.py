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

    @property
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
        center = self.center
        return (
            Rectangle(self.pt1.x, center.y, center.x, self.pt2.y),  # A
            Rectangle(center.x, center.y, self.pt2.x, self.pt2.y),  # B
            Rectangle(center.x, self.pt1.y, self.pt2.x, center.y),  # C
            Rectangle(self.pt1.x, self.pt1.y, center.x, center.y),  # D
        )

    @classmethod
    def from_points(cls, points):
        point1, point2 = points
        if not (isinstance(point1, Point) and isinstance(point2, Point)):
            raise ValueError("Argument is not iterable of points")
        return cls(point1.x, point1.y, point2.x, point2.y)

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomleft(self):
        return Point(self.pt1.x, self.pt1.y)

    @property
    def topright(self):
        return Point(self.pt2.x, self.pt2.y)

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)
