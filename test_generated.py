```python
import unittest
import os
import sys
from unittest.mock import patch
from io import StringIO

# Add the project root to the Python path so that imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../sample_repo')))  # Adjust path if needed
from my_module import add, subtract, divide, multiply, greet

class TestMyModule(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)
        self.assertEqual(add(-2, 3), 1)

    def test_add_zero(self):
        self.assertEqual(add(2, 0), 2)
        self.assertEqual(add(0, 2), 2)
        self.assertEqual(add(0, 0), 0)

    def test_add_large_numbers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)

    def test_add_float_numbers(self):
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(add(2.1, 3.2), 5.3)


    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(-5, 3), -8)

    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_subtract_large_numbers(self):
        self.assertEqual(subtract(2000000, 1000000), 1000000)

    def test_subtract_float_numbers(self):
        self.assertAlmostEqual(subtract(5.5, 3.5), 2.0)
        self.assertAlmostEqual(subtract(5.2, 3.1), 2.1)

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-6, -3), 2)

    def test_divide_mixed_numbers(self):
        self.assertEqual(divide(6, -3), -2)
        self.assertEqual(divide(-6, 3), -2)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_divide_float_numbers(self):
        self.assertAlmostEqual(divide(5.5, 2.0), 2.75)
        self.assertAlmostEqual(divide(6.0, 4.0), 1.5)

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(-2, 3), -6)

    def test_multiply_zero(self):
        self.assertEqual(multiply(2, 0), 0)
        self.assertEqual(multiply(0, 2), 0)
        self.assertEqual(multiply(0, 0), 0)

    def test_multiply_large_numbers(self):
        self.assertEqual(multiply(1000, 1000), 1000000)

    def test_multiply_float_numbers(self):
        self.assertAlmostEqual(multiply(2.5, 3.0), 7.5)
        self.assertAlmostEqual(multiply(2.1, 3.2), 6.72)


    def test_greet_with_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_empty_name(self):
        self.assertEqual(greet(""), "Hello, !")

    def test_greet_with_number(self):
        self.assertEqual(greet(123), "Hello, 123!")

    def test_greet_with_special_characters(self):
        self.assertEqual(greet("!@#$%^"), "Hello, !@#$%^!")

    @patch('builtins.input', return_value='Bob')
    @patch('sys.stdout', new_callable=StringIO)
    def test_greet_with_input(self, stdout, mock_input):
        greet_return = greet(mock_input())
        self.assertEqual(greet_return, "Hello, Bob!")
        self.assertEqual(stdout.getvalue(), "") #Ensure no output to console in this mocked scenario. The greet function itself doesn't print to stdout.
```