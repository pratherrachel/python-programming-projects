"""Unit tests for SmartFit's enrollment policy and pricing."""

import unittest

from smartfit import fitness_program, monthly_price, requires_clearance


class SmartFitTests(unittest.TestCase):
    def test_age_boundaries(self):
        self.assertEqual(fitness_program(17), "Teen Fitness Program")
        self.assertEqual(fitness_program(18), "Regular Fitness Program")
        self.assertEqual(fitness_program(40), "Regular Fitness Program")
        self.assertEqual(fitness_program(41), "Senior Wellness Program")
        with self.assertRaises(ValueError):
            fitness_program(-1)

    def test_clearance_policy(self):
        self.assertFalse(requires_clearance(39, True))
        self.assertTrue(requires_clearance(40, True))
        self.assertFalse(requires_clearance(40, False))

    def test_membership_pricing(self):
        self.assertEqual(monthly_price("basic", 25), 30.0)
        self.assertEqual(monthly_price("basic", 25, True), 45.0)
        self.assertEqual(monthly_price("premium", 29), 54.0)
        self.assertEqual(monthly_price("premium", 30), 60.0)
        with self.assertRaises(ValueError):
            monthly_price("other", 25)


if __name__ == "__main__":
    unittest.main()
