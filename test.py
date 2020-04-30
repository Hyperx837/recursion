import unittest
from . import recursion


class TestRecurse(unittest.TestCase):
    def test_pow(self):
        self.assertEqual(recursion.recur_pow(3, 3), 3 ** 3, 'Test Case Failed')
        self.assertEqual(recursion.recur_pow(2, -3), 2 ** -3, 'Test Case Failed')
        self.assertEqual(recursion.recur_pow(3, 0), 3 ** 0, 'Test Case Failed')
        self.assertEqual(recursion.recur_pow(-4, 16), (-4) ** 16, 'Test Case Failed')
        self.assertEqual(recursion.recur_pow(5, -4), 5 ** -4, 'Test Case Failed')

    def test_fib(self):
        self.assertEqual(recursion.fib(3), 2, 'Test Case Failed')
        self.assertEqual(recursion.fib(6), 8, 'Test Case Failed')
        self.assertEqual(recursion.fib(7), 13, 'Test Case Failed')


if __name__ == '__main__':
    unittest.main()
