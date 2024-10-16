import unittest
import math
from calculator import *

class TestAdvancedCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = AdvancedCalculator()

    # Test for basic operations
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5, "Addition of 2 and 3 should be 5")
        self.assertEqual(self.calc.add(-1, 1), 0, "Addition of -1 and 1 should be 0")
        self.assertEqual(self.calc.add(0, 0), 0, "Addition of 0 and 0 should be 0")

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2, "Subtraction of 5 and 3 should be 2")
        self.assertEqual(self.calc.subtract(-1, 1), -2, "Subtraction of -1 and 1 should be -2")
        self.assertEqual(self.calc.subtract(0, 0), 0, "Subtraction of 0 and 0 should be 0")

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12, "Multiplication of 4 and 3 should be 12")
        self.assertEqual(self.calc.multiply(-2, 2), -4, "Multiplication of -2 and 2 should be -4")
        self.assertEqual(self.calc.multiply(0, 1), 0, "Multiplication of 0 and 1 should be 0")

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5, "Division of 10 by 2 should be 5")
        self.assertEqual(self.calc.divide(3, 2), 1.5, "Division of 3 by 2 should be 1.5")
        self.assertEqual(self.calc.divide(1, 0), 'undefined', "Division by zero should return 'undefined'")

    # Test for powers and roots
    def test_square(self):
        self.assertEqual(self.calc.square(4), 16, "Square of 4 should be 16")
        self.assertEqual(self.calc.square(-3), 9, "Square of -3 should be 9")
        self.assertEqual(self.calc.square(0), 0, "Square of 0 should be 0")

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8, "2 raised to the power of 3 should be 8")
        self.assertEqual(self.calc.power(5, 0), 1, "5 raised to the power of 0 should be 1")
        self.assertEqual(self.calc.power(-2, 2), 4, "Negative 2 raised to the power of 2 should be 4")

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(16), 4, "Square root of 16 should be 4")
        self.assertEqual(self.calc.square_root(0), 0, "Square root of 0 should be 0")
        self.assertEqual(self.calc.square_root(-1), 'undefined', "Square root of a negative number should return 'undefined'")

    def test_nth_root(self):
        self.assertEqual(self.calc.nth_root(8, 3), 2, "Cube root of 8 should be 2")
        self.assertEqual(self.calc.nth_root(16, 4), 2, "Fourth root of 16 should be 2")
        self.assertEqual(self.calc.nth_root(-8, 3), -2, "Cube root of -8 should be -2")
        self.assertEqual(self.calc.nth_root(-16, 2), 'undefined', "Even root of negative number should return 'undefined'")

    # Test trigonometric functions
    def test_sin(self):
        self.assertAlmostEqual(self.calc.sin(math.pi / 2), 1, msg="sin(pi/2) should be 1")
        self.assertAlmostEqual(self.calc.sin(math.pi), 0, msg="sin(pi) should be 0")

    def test_cos(self):
        self.assertAlmostEqual(self.calc.cos(0), 1, msg="cos(0) should be 1")
        self.assertAlmostEqual(self.calc.cos(math.pi), -1, msg="cos(pi) should be -1")

    def test_tan(self):
        self.assertAlmostEqual(self.calc.tan(0), 0, msg="tan(0) should be 0")
        self.assertAlmostEqual(self.calc.tan(math.pi / 4), 1, msg="tan(pi/4) should be 1")

    # Test preprocess_expression method
    def test_preprocess_expression(self):
        expr = "3^2 + 2√16"
        expected = "3**2 + (16 ** (1/2))"
        self.assertEqual(self.calc.preprocess_expression(expr), expected, "Preprocessing '3^2 + 2√16' should return '3**2 + (16 ** (1/2))'")

    # Test expression evaluation
    def test_evaluate_expression(self):
        expr1 = "3 + 5 ✕ 2"
        expr2 = "2^3 + 4"
        expr3 = "9 ➗ 3 - 1"

        self.assertEqual(self.calc.evaluate_expression(expr1), 13, "Evaluation of '3 + 5 ✕ 2' should be 13")
        self.assertEqual(self.calc.evaluate_expression(expr2), 12, "Evaluation of '2^3 + 4' should be 12")
        self.assertEqual(self.calc.evaluate_expression(expr3), 2, "Evaluation of '9 ➗ 3 - 1' should be 2")

    def test_overflow(self):
        # Test for large exponentiation that causes overflow
        expression = "1e308 ** 2"  # This will likely cause an OverflowError
        result = self.calc.evaluate_expression(expression)
        self.assertEqual(result, 'overflow')

    def test_large_multiplication(self):
        result = self.calc.evaluate_expression("1e154 * 1e154")
        self.assertEqual(result, 1e308)  # Should handle large numbers without overflow

    def testSampleTest1(self):
        expression = "((3.5 + 4.9) - (10➗2)) ✕ 3.40"
        result = self.calc.evaluate_expression(expression)
        self.assertEqual(result, 11.56)
        
    def testSampleTest2(self):
        expression = "9999**9"
        result = self.calc.evaluate_expression(expression)
        self.assertEqual(result, 999100359916012598740083996400089999)

if __name__ == '__main__':
    unittest.main()
