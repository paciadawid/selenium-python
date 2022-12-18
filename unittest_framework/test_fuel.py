import unittest

from basics.functions import calculate_fuel


class FuelTests(unittest.TestCase):

    def test_12(self):
        self.assertEqual(2, calculate_fuel(12))

    def test_string(self):
        self.assertEqual(False, calculate_fuel("test"))

    def test_negative_value(self):
        self.assertEqual(False, calculate_fuel(-1))

    def test_zero(self):
        self.assertEqual(False, calculate_fuel(0))

    def test_1(self):
        self.assertEqual(1, calculate_fuel(1))


if __name__ == '__main__':
    unittest.main()
