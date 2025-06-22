```python
import unittest
import os
import sys
import io
from contextlib import redirect_stdout

# Dynamically add the repository to the Python path
# This is a workaround as we don't know where the repository will be cloned.
repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PRATICK-sample_repo"))
sys.path.insert(0, repo_path)


from main import add, subtract, divide, multiply, greet, process_numbers

class TestMainFunctions(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, 0), 0)

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

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(multiply(2, -3), -6)

    def test_multiply_zero(self):
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(0, 0), 0)

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-6, -3), 2)

    def test_divide_mixed_numbers(self):
        self.assertEqual(divide(6, -3), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide(5, 0)
        self.assertTrue("Cannot divide by zero" in str(context.exception))

    def test_divide_zero_by_number(self):
        self.assertEqual(divide(0, 5), 0)

    def test_greet_with_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_with_empty_name(self):
        self.assertEqual(greet(""), "Hello, !")

    def test_greet_with_none_name(self):
        self.assertEqual(greet(None), "Hello, None!")  # Handle None input

    def test_process_numbers_valid_input(self):
        numbers = [1, 2, 3, 4, 5]
        expected_output = sum(numbers) / len(numbers)
        self.assertEqual(process_numbers(numbers), expected_output)

    def test_process_numbers_empty_list(self):
        with self.assertRaises(ValueError) as context:
            process_numbers([])
        self.assertTrue("Input list cannot be empty" in str(context.exception))

    def test_process_numbers_non_numeric_input(self):
         with self.assertRaises(TypeError) as context:
             process_numbers([1, 2, "a", 4, 5])
         self.assertTrue("Elements of the list must be numeric" in str(context.exception))

    def test_process_numbers_mixed_numeric_types(self):
        numbers = [1, 2.5, 3, 4.2, 5]
        expected_output = sum(numbers) / len(numbers)
        self.assertEqual(process_numbers(numbers), expected_output)

    def test_process_numbers_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5]
        expected_output = sum(numbers) / len(numbers)
        self.assertEqual(process_numbers(numbers), expected_output)

if __name__ == '__main__':
    unittest.main()
```