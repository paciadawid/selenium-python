import unittest

from basics.classes import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add_values(self):
        self.assertEqual(3, self.calculator.add(1, 2))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
