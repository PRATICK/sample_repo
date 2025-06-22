```python
import unittest
import os
import sys
import io
from contextlib import redirect_stdout

# Dynamically add the project directory to the Python path
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'PRATICK-sample_repo'))
sys.path.insert(0, PROJECT_PATH)

# Now you can import from your project without PYTHONPATH issues.
from main import greet, calculate_sum, divide, read_file  # Replace 'main' with the actual module name


class TestMain(unittest.TestCase):

    def test_greet_with_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_without_name(self):
        self.assertEqual(greet(None), "Hello, World!")
        self.assertEqual(greet(""), "Hello, World!")  # Added empty string test

    def test_calculate_sum_positive_numbers(self):
        self.assertEqual(calculate_sum(2, 3), 5)

    def test_calculate_sum_negative_numbers(self):
        self.assertEqual(calculate_sum(-2, -3), -5)

    def test_calculate_sum_mixed_numbers(self):
        self.assertEqual(calculate_sum(-2, 3), 1)

    def test_calculate_sum_zero(self):
        self.assertEqual(calculate_sum(0, 0), 0)
        self.assertEqual(calculate_sum(5, 0), 5)
        self.assertEqual(calculate_sum(0, 5), 5)


    def test_divide_valid_division(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)

    def test_read_file_existing_file(self):
        # Create a temporary file for testing
        with open("temp_test_file.txt", "w") as f:
            f.write("This is a test file.")

        content = read_file("temp_test_file.txt")
        self.assertEqual(content, "This is a test file.")

        # Clean up the temporary file
        os.remove("temp_test_file.txt")

    def test_read_file_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_file("nonexistent_file.txt")

    def test_read_file_empty_file(self):
        # Create an empty temporary file
        with open("empty_test_file.txt", "w") as f:
            pass  # Create an empty file

        content = read_file("empty_test_file.txt")
        self.assertEqual(content, "")

        # Clean up the temporary file
        os.remove("empty_test_file.txt")


    def test_greet_type_validation(self):
        with self.assertRaises(TypeError):
            greet(123) # Test with an integer
        with self.assertRaises(TypeError):
            greet([1,2,3]) # Test with a list
        with self.assertRaises(TypeError):
            greet({'key':'value'}) # Test with a dictionary

    def test_calculate_sum_type_validation(self):
        with self.assertRaises(TypeError):
            calculate_sum("1", 2)
        with self.assertRaises(TypeError):
            calculate_sum(1, "2")
        with self.assertRaises(TypeError):
            calculate_sum([1,2,3], 2)

    def test_divide_type_validation(self):
         with self.assertRaises(TypeError):
            divide("1", 2)
         with self.assertRaises(TypeError):
            divide(1, "2")
         with self.assertRaises(TypeError):
            divide([1,2,3], 2)

    def test_read_file_type_validation(self):
        with self.assertRaises(TypeError):
            read_file(123)
        with self.assertRaises(TypeError):
            read_file([1,2,3])

if __name__ == '__main__':
    unittest.main()
```