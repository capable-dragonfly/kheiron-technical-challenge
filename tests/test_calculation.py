import unittest
from calculation.calculation import resolve_calculation

class TestPrefixCalculation(unittest.TestCase):
    def test_addition(self):
        test_input = '+ 3 5'
        expected_result = 8

        test_result = resolve_calculation(test_input, notation='prefix')

        self.assertEqual(test_result, expected_result)

    def test_substraction(self):
        test_input = '- 3 5'
        expected_result = -2

        test_result = resolve_calculation(test_input, notation='prefix')

        self.assertEqual(test_result, expected_result)

    def test_multiplication(self):
        test_input = '* 3 5'
        expected_result = 15

        test_result = resolve_calculation(test_input, notation='prefix')

        self.assertEqual(test_result, expected_result)

    def test_division(self):
        test_input = '/ 11 5'
        expected_result = 2

        test_result = resolve_calculation(test_input, notation='prefix')

        self.assertEqual(test_result, expected_result)

    def test_multiple_operators(self):
        test_input = '- / 10 + 1 1 * 1 2'
        expected_result = 3

        test_result = resolve_calculation(test_input, notation='prefix')

        self.assertEqual(test_result, expected_result)

class TestInfixCalculation(unittest.TestCase):
    def test_addition(self):
        test_input = '( 3 + 5 )'
        expected_result = 8

        test_result = resolve_calculation(test_input, notation='infix')

        self.assertEqual(test_result, expected_result)

    def test_substraction(self):
        test_input = '( 3 - 5 )'
        expected_result = -2

        test_result = resolve_calculation(test_input, notation='infix')

        self.assertEqual(test_result, expected_result)

    def test_multiplication(self):
        test_input = '( 3 * 5 )'
        expected_result = 15

        test_result = resolve_calculation(test_input, notation='infix')

        self.assertEqual(test_result, expected_result)

    def test_division(self):
        test_input = '( 11 / 5 )'
        expected_result = 2

        test_result = resolve_calculation(test_input, notation='infix')

        self.assertEqual(test_result, expected_result)

    def test_multiple_operators(self):
        test_input = '( ( ( 10 + 6 ) / 3 ) - ( 2 * 3 ) )'
        expected_result = -1

        test_result = resolve_calculation(test_input, notation='infix')

        self.assertEqual(test_result, expected_result)
