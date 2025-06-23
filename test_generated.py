```python
import unittest
import os
import sys

# Add the project root to the Python path to import the module directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sample_repo')))

# Now we can import the modules from the sample_repo directory
from sample_repo import my_module


class TestMyModuleFunctions(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(my_module.add(2, 3), 5)
        self.assertEqual(my_module.add(10, 20), 30)

    def test_add_negative_numbers(self):
        self.assertEqual(my_module.add(-2, -3), -5)
        self.assertEqual(my_module.add(-10, -20), -30)

    def test_add_mixed_numbers(self):
        self.assertEqual(my_module.add(2, -3), -1)
        self.assertEqual(my_module.add(-10, 20), 10)

    def test_add_zero(self):
        self.assertEqual(my_module.add(0, 5), 5)
        self.assertEqual(my_module.add(5, 0), 5)
        self.assertEqual(my_module.add(0, 0), 0)

    def test_greet_with_name(self):
        self.assertEqual(my_module.greet("Alice"), "Hello, Alice!")
        self.assertEqual(my_module.greet("Bob"), "Hello, Bob!")

    def test_greet_empty_name(self):
        self.assertEqual(my_module.greet(""), "Hello, !")

    def test_greet_name_with_spaces(self):
        self.assertEqual(my_module.greet("  Alice  "), "Hello,   Alice  !")

    def test_calculate_area_positive_side(self):
        self.assertEqual(my_module.calculate_area(5), 25)
        self.assertEqual(my_module.calculate_area(10), 100)

    def test_calculate_area_zero_side(self):
        self.assertEqual(my_module.calculate_area(0), 0)

    def test_calculate_area_negative_side(self):
        with self.assertRaises(ValueError):
            my_module.calculate_area(-5)

    def test_is_even_even_number(self):
        self.assertTrue(my_module.is_even(4))
        self.assertTrue(my_module.is_even(0))
        self.assertTrue(my_module.is_even(-2))

    def test_is_even_odd_number(self):
        self.assertFalse(my_module.is_even(3))
        self.assertFalse(my_module.is_even(-1))


if __name__ == '__main__':
    unittest.main()
```