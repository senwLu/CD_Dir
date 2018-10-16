import unittest
from Modules.mathDojoTDD import *

x = MathDojo()


class addTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(x.add(2, 3, 5, 1), 11)

    def test2(self):
        self.assertEqual(x.add(1, 2), 3)

    def test3(self):
        self.assertEqual(x.add(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
