# Stworzyć plik polys.py i zapisać w nim funkcje do działań na wielomianach.
# Wielomian będzie reprezentowany przez listę swoich współczynników, np. [a0, a1, a2] dla a0 + a1*x + a2*x*x.
# Napisać kod testujący moduł polys.

from polys import *
import unittest


class TestPolynomials(unittest.TestCase):
    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2
        self.p3 = [2, 1]  # x+2
        self.p4 = [3, 2]  # 2x+3

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])  # x^2 + x
        self.assertEqual(add_poly(self.p2, self.p1), [0, 1, 1])  # x^2 + x
        self.assertEqual(add_poly(self.p3, self.p4), [5, 3])  # 3x+5
        self.assertEqual(add_poly(self.p4, self.p3), [5, 3])  # 3x+5

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])  # -x^2 + x
        self.assertEqual(sub_poly(self.p2, self.p1), [0, -1, 1])  # x^2 - x
        self.assertEqual(sub_poly(self.p3, self.p4), [-1, -1])  # -x -1
        self.assertEqual(sub_poly(self.p4, self.p3), [1, 1])  # x + 1

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])  # x^3
        self.assertEqual(mul_poly(self.p2, self.p1), [0, 0, 0, 1])  # x^3
        self.assertEqual(mul_poly(self.p3, self.p4), [6, 7, 2])  # 2x^2 + 7x + 6
        self.assertEqual(mul_poly(self.p4, self.p3), [6, 7, 2])  # 2x^2 + 7x + 6

    def test_is_zero(self):
        self.assertEqual(is_zero([0]), True)
        self.assertEqual(is_zero([0, 0, 0]), True)
        self.assertEqual(is_zero([0, 0, 0, 0, -1, 0]), False)

    def test_eq_poly(self):
        self.assertEqual(eq_poly([1], [1, 0, 0]), True)
        self.assertEqual(eq_poly([0, 1, 0], [0, 1, 0, 0]), True)
        self.assertEqual(eq_poly([1], [0, 1]), False)

    def test_eval_poly(self): pass

    def test_combine_poly(self): pass

    def test_pow_poly(self): pass

    def test_diff_poly(self): pass

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy