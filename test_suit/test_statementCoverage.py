import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_suit.isTriangle import Triangle

class TestTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(Triangle.classify(10, 10, 10), Triangle.Type.EQUILATERAL)

    def test_isosceles(self):
        self.assertEqual(Triangle.classify(10, 10, 5), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(10, 5, 10), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 10, 10), Triangle.Type.ISOSCELES)

    def test_scalene(self):
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)

    def test_invalid(self):
        self.assertEqual(Triangle.classify(0, 10, 10), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1, 10, 10), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(10, 0, 10), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(10, 10, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 3, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(3, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 2, 4), Triangle.Type.INVALID)

if __name__ == '__main__':
    unittest.main()