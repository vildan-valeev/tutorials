import unittest
from .fizz_buzz import fizz_buzz


class FizzBuzzTest(unittest.TestCase):

    def test_fizz(self):
        number = 6
        b = 'Buzz'
        result = fizz_buzz(number)
        self.assertEqual(result, b)

    def test_buzz(self):
        number = 10
        f = 'Fizz'
        result = fizz_buzz(number)
        self.assertEqual(result, f)

    def test_fb(self):
        number = 15
        fb = 'FizzBuzz'
        result = fizz_buzz(number)
        self.assertEqual(result, fb)

    # def test_type(self):

if __name__ == '__main__':
    unittest.main()