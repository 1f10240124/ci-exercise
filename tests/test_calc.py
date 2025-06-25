import unittest
from project.calc import gcd

class TestTarget(unittest.TestCase):
    def test_fact_positive(self):
        self.assertEqual(gcd(1), 1)
        self.assertEqual(gcd(5), 120)

    def test_fact_zero(self):
        self.assertEqual(gcd(0), 1)

    def test_fact_negative(self):
        with self.assertRaises(ValueError):
            gcd(-1)


class TestCalc(unittest.TestCase):

    def test_gcd_positive(self):
        self.assertEqual(gcd(7, 3), 1)
        self.assertEqual(gcd(56, 98), 14)

    def test_gcd_negative(self):
        self.assertEqual(gcd(-15, -25), 5)
        self.assertEqual(gcd(-24, 32), 8)

    def test_gcd_zero(self):
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 7), 7)
        self.assertEqual(gcd(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
