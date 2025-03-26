import unittest
from isTriangle import Triangle

class TestMutationAdequate(unittest.TestCase):
    def test_invalid_triangle(self):
        self.assertEqual(Triangle.classify(0, 0, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1, 2, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)

    def test_scalene_triangle(self):
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)

    def test_equilateral_triangle(self):
        self.assertEqual(Triangle.classify(5, 5, 5), Triangle.Type.EQUILATERAL)

    def test_isosceles_triangle(self):
        self.assertEqual(Triangle.classify(5, 5, 8), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 8, 5), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(8, 5, 5), Triangle.Type.ISOSCELES)

if __name__ == '__main__':
    unittest.main()