import unittest
import sys
import os
from prime import isPrime, isPrime2

class TestPrimeFunctions(unittest.TestCase):
    
    def test_isPrime(self):
        self.assertFalse(isPrime(1))  # 1 no es primo
        self.assertTrue(isPrime(2))   # 2 es primo
        self.assertTrue(isPrime(3))   # 3 es primo
        self.assertFalse(isPrime(4))  # 4 no es primo
        self.assertTrue(isPrime(5))   # 5 es primo
        self.assertFalse(isPrime(20)) # 20 no es primo
        self.assertFalse(isPrime(21)) # 21 no es primo
        self.assertTrue(isPrime(23))  # 23 es primo
        self.assertFalse(isPrime(24)) # 24 no es primo

    def test_isPrime2(self):
        self.assertFalse(isPrime2(1))  # 1 no es primo
        self.assertTrue(isPrime2(2))   # 2 es primo
        self.assertTrue(isPrime2(3))   # 3 es primo
        self.assertFalse(isPrime2(4))  # 4 no es primo
        self.assertTrue(isPrime2(5))   # 5 es primo
        self.assertFalse(isPrime2(20)) # 20 no es primo
        self.assertFalse(isPrime2(21)) # 21 no es primo
        self.assertTrue(isPrime2(23))  # 23 es primo
        self.assertFalse(isPrime2(24)) # 24 no es primo

if __name__ == '__main__':
    unittest.main()
