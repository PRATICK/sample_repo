```python
import unittest
import sys
import os

# Dynamically add the project directory to sys.path to allow imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sample_repo import my_math_library  # Import the library to test
from sample_repo import my_string_library


class TestMyMathLibrary(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(my_math_library.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(my_math_library.add(-2, -3), -5)

    def test_add_positive_and_negative(self):
        self.assertEqual(my_math_library.add(5, -2), 3)

    def test_add_zero(self):
        self.assertEqual(my_math_library.add(5, 0), 5)
        self.assertEqual(my_math_library.add(0, 5), 5)

    def test_add_large_numbers(self):
        self.assertEqual(my_math_library.add(1000000, 2000000), 3000000)

    def test_subtract_positive_numbers(self):
        self.assertEqual(my_math_library.subtract(5, 2), 3)

    def test_subtract_negative_numbers(self):
        self.assertEqual(my_math_library.subtract(-5, -2), -3)

    def test_subtract_positive_and_negative(self):
        self.assertEqual(my_math_library.subtract(5, -2), 7)

    def test_subtract_zero(self):
        self.assertEqual(my_math_library.subtract(5, 0), 5)
        self.assertEqual(my_math_library.subtract(0, 5), -5)

    def test_subtract_large_numbers(self):
        self.assertEqual(my_math_library.subtract(2000000, 1000000), 1000000)

    def test_multiply_positive_numbers(self):
         self.assertEqual(my_math_library.multiply(5, 2), 10)

    def test_multiply_negative_numbers(self):
        self.assertEqual(my_math_library.multiply(-5, -2), 10)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(my_math_library.multiply(5, -2), -10)

    def test_multiply_zero(self):
        self.assertEqual(my_math_library.multiply(5, 0), 0)
        self.assertEqual(my_math_library.multiply(0, 5), 0)

    def test_multiply_large_numbers(self):
        self.assertEqual(my_math_library.multiply(1000, 1000), 1000000)

    def test_divide_positive_numbers(self):
        self.assertEqual(my_math_library.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(my_math_library.divide(-10, -2), 5)

    def test_divide_positive_and_negative(self):
        self.assertEqual(my_math_library.divide(10, -2), -5)

    def test_divide_by_one(self):
        self.assertEqual(my_math_library.divide(10, 1), 10)

    def test_divide_zero(self):
       with self.assertRaises(ZeroDivisionError):
           my_math_library.divide(5,0)

    def test_divide_floating_point(self):
        self.assertEqual(my_math_library.divide(5, 2), 2.5)


class TestMyStringLibrary(unittest.TestCase):

    def test_reverse_string_normal(self):
        self.assertEqual(my_string_library.reverse_string("hello"), "olleh")

    def test_reverse_string_empty(self):
        self.assertEqual(my_string_library.reverse_string(""), "")

    def test_reverse_string_palindrome(self):
        self.assertEqual(my_string_library.reverse_string("madam"), "madam")

    def test_reverse_string_with_spaces(self):
        self.assertEqual(my_string_library.reverse_string("hello world"), "dlrow olleh")

    def test_reverse_string_single_char(self):
        self.assertEqual(my_string_library.reverse_string("a"), "a")

    def test_is_palindrome_normal(self):
        self.assertTrue(my_string_library.is_palindrome("madam"))

    def test_is_palindrome_case_insensitive(self):
        self.assertTrue(my_string_library.is_palindrome("Madam"))  # Assuming case-insensitive check in impl.
        self.assertTrue(my_string_library.is_palindrome("Racecar"))

    def test_is_palindrome_with_spaces(self):
        self.assertFalse(my_string_library.is_palindrome("madam i'm adam")) #Assuming spaces are significant.

    def test_is_palindrome_empty_string(self):
        self.assertTrue(my_string_library.is_palindrome(""))  #Empty string is a palindrome.

    def test_is_palindrome_non_palindrome(self):
        self.assertFalse(my_string_library.is_palindrome("hello"))

if __name__ == '__main__':
    unittest.main()
```