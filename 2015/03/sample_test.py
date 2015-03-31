import unittest
from itertools import islice
import solution


def multiples_of(num):
    i = 1
    while True:
        yield num * i
        i += 1


def ones():
    while True:
        yield 1


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        fibonacci = solution.fibonacci()
        first_five = list(islice(fibonacci, 5))
        self.assertEqual(first_five, [1, 1, 2, 3, 5])


class TestPrimes(unittest.TestCase):
    def test_primes(self):
        primes = solution.primes()
        first_five = list(islice(primes, 5))
        self.assertEqual(first_five, [2, 3, 5, 7, 11])


class TestAlphabet(unittest.TestCase):
    def test_alphabet(self):
        alphabet = solution.alphabet(code='lat')
        first_five = list(islice(alphabet, 5))
        self.assertEqual(first_five, ['a', 'b', 'c', 'd', 'e'])


class TestIntertwine(unittest.TestCase):
    def test_intertwine(self):
        fibonacci_3_prime_3_bg_3 = solution.intertwined_sequences([
            {'sequence': 'fibonacci', 'length': 3},
            {'sequence': 'primes', 'length': 3},
            {'sequence': 'alphabet', 'code': 'bg', 'length': 3}
        ])

        self.assertEqual(
            list(fibonacci_3_prime_3_bg_3),
            [1, 1, 2, 2, 3, 5, 'а', 'б', 'в']
        )

    
    def test_with_generator_definitions(self):
        with_generator_definitions = intertwined_sequences(
            [
                {'sequence': 'multiples_of', 'length': 3, 'num': 12},
                {'sequence': 'ones', 'length': 3},
                {'sequence': 'multiples_of', 'length': 3}
            ],
            generator_definitions={
                'multiples_of': multiples_of,
                'ones': ones
            }
        )
        self.assertEqual(
            list(with_generator_definitions),
            [12, 24, 36, 1, 1, 1, 48, 60, 72]
        )


if __name__ == '__main__':
    unittest.main()
