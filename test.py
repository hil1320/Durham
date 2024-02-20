# filename: minimum_and_test.py
import unittest


def find_minimum(numbers):
    if not numbers or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input list must contain only integers")

    min_element = numbers[0]

    for num in numbers:
        if num < min_element:
            min_element = num

    return min_element


class TestMinimumFunction(unittest.TestCase):

    def test_short_list(self):
        self.assertEqual(find_minimum([90]), 90)
        self.assertEqual(find_minimum([12, 10]), 10)
        self.assertEqual(find_minimum([10, 12]), 10)
        self.assertEqual(find_minimum([12, 14, 36]), 12)
        self.assertEqual(find_minimum([36, 14, 12]), 12)
        self.assertEqual(find_minimum([14, 12, 36]), 12)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_minimum([])

    def test_min_first_last(self):
        self.assertEqual(find_minimum([10, 23, 34, 81, 97]), 10)
        self.assertEqual(find_minimum([97, 81, 34, 23, 10]), 10)

    def test_min_negative(self):
        self.assertEqual(find_minimum([10, -2, 5, 23]), -2)
        self.assertEqual(find_minimum([10, -2, -24, 4]), -24)

    def test_all_negative(self):
        self.assertEqual(find_minimum([-23, -31, -45, -56]), -56)
        self.assertEqual(find_minimum([-6, -203, -2, -78]), -203)

    def test_real_numbers(self):
        with self.assertRaises(ValueError):
            find_minimum([23, 34.56, 67, 33])

    def test_alphabetic_special_chars(self):
        with self.assertRaises(ValueError):
            find_minimum([23, 'hi', 32, 1])
        with self.assertRaises(ValueError):
            find_minimum([12, '&', '*', '34m', '!'])

    def test_duplicate_elements(self):
        self.assertEqual(find_minimum([3, 4, 6, 9, 6]), 3)
        self.assertEqual(find_minimum([13, 6, 6, 9, 15]), 6)

    def test_large_value(self):
        self.assertEqual(find_minimum([530, 429449672, 97, 23, 46, 59]), 23)


if __name__ == '__main__':
    unittest.main()
