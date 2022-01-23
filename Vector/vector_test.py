import unittest
from Vector import vector

class TestVector(unittest.TestCase)
    def test_constrtuctor(self):
        p = Point()
        self.assertEqual(p.x, 0.0)
        self.assertEqual(p.y, 0.0)

        p = Point(2, 19)
        self.assertEqual(p.x, 2.0)
        self.assertEqual(p.y, 19.0)

        with self.assertRaises(TypeError):
            Point(Point(), 0.0)

        with self.assertRaises(ValueError):
            Point('abc', 0.0)
