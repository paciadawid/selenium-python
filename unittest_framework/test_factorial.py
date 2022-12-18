import unittest

from basics.factorial import factorial


class MyTestCase(unittest.TestCase):

    def test_10(self):
        self.assertEqual(3628800, factorial(10))

    def test_2(self):
        self.assertEqual(2, factorial(2))

    def test_1(self):
        self.assertEqual(1, factorial(1))

    def test_0(self):
        self.assertEqual(1, factorial(0))

    def test_negative(self):
        self.assertEqual(False, factorial(-1))

    def test_string(self):
        self.assertEqual(False, factorial("test"))

    def test_float(self):
        self.assertEqual(False, factorial(1.5))


if __name__ == '__main__':
    unittest.main()
