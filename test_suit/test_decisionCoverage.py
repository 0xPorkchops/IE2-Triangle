import unittest
from isTriangle import Triangle

class TestDecisionCoverage(unittest.TestCase):
    def test_valid_scalene_triangle(self):
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)

    def test_valid_isosceles_triangle(self):
        self.assertEqual(Triangle.classify(5, 5, 8), Triangle.Type.ISOSCELES)

    def test_valid_equilateral_triangle(self):
        self.assertEqual(Triangle.classify(6, 6, 6), Triangle.Type.EQUILATERAL)

    def test_invalid_zero_side(self):
        self.assertEqual(Triangle.classify(0, 4, 5), Triangle.Type.INVALID)

    def test_invalid_negative_side(self):
        self.assertEqual(Triangle.classify(-3, 4, 5), Triangle.Type.INVALID)

    def test_invalid_sum_of_two_sides_equal_to_third(self):
        self.assertEqual(Triangle.classify(2, 2, 4), Triangle.Type.INVALID)

    def test_invalid_sum_of_two_sides_less_than_third(self):
        self.assertEqual(Triangle.classify(1, 2, 4), Triangle.Type.INVALID)

if __name__ == "__main__":
    unittest.main()
