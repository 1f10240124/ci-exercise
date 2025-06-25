import unittest
from project.calc import fact

class TestTarget(unittest.TestCase):
    def test_fact_positive(self):
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(5), 120)

    def test_fact_zero(self):
        self.assertEqual(fact(0), 1)

    def test_fact_negative(self):
        with self.assertRaises(ValueError):
            fact(-1)


class TestCalc(unittest.TestCase):

    def test_gcd_positive(self):
        self.assertEqual(fact(7, 3), 1)
        self.assertEqual(fact(56, 98), 14)

    def test_gcd_negative(self):
        self.assertEqual(fact(-15, -25), 5)
        self.assertEqual(fact(-24, 32), 8)

    def test_gcd_zero(self):
        self.assertEqual(fact(5, 0), 5)
        self.assertEqual(fact(0, 7), 7)
        self.assertEqual(fact(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
