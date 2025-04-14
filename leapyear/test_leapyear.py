# -*- coding: utf-8 -*-
'''
Unit test for leapyear.py
Student version
'''

import unittest
import leapyear

# Test class for general input validation and known edge cases
class LeapYearValidationTest(unittest.TestCase):
    # Test a valid leap year (divisible by 400)
    def test_valid_leap_year(self):
        self.assertTrue(leapyear.to_leap_year(2000))

    # Test a valid non-leap year (divisible by 100 but not by 400)
    def test_valid_non_leap_year(self):
        self.assertFalse(leapyear.to_leap_year(1900))

    # Test that a string input raises NotIntegerError
    def test_invalid_input_string(self):
        with self.assertRaises(leapyear.NotIntegerError):
            leapyear.to_leap_year("2000")

    # Test that a float input raises NotIntegerError
    def test_invalid_input_float(self):
        with self.assertRaises(leapyear.NotIntegerError):
            leapyear.to_leap_year(2000.5)

    # Test that a negative year raises OutOfRangeError
    def test_invalid_input_negative(self):
        with self.assertRaises(leapyear.OutOfRangeError):
            leapyear.to_leap_year(-2000)

    # Test that the year 0 raises OutOfRangeError (leap years start from year 1)
    def test_invalid_input_zero(self):
        with self.assertRaises(leapyear.OutOfRangeError):
            leapyear.to_leap_year(0)

    # Test that None input raises NotIntegerError
    def test_invalid_input_none(self):
        with self.assertRaises(leapyear.NotIntegerError):
            leapyear.to_leap_year(None)

    # Test that a list as input raises NotIntegerError
    def test_invalid_input_list(self):
        with self.assertRaises(leapyear.NotIntegerError):
            leapyear.to_leap_year([2000])

    # Test that a dictionary as input raises NotIntegerError
    def test_invalid_input_dict(self):
        with self.assertRaises(leapyear.NotIntegerError):
            leapyear.to_leap_year({2000: "year"})

# Test class for edge case years that are or are not leap years
class LeapYearEdgeCasesTest(unittest.TestCase):
    # Test a list of known leap years
    def test_leap_years_in_range(self):
        # Years that are leap years
        leap_years = [
            4, 8, 1600, 2000, 2400, 1904, 1908, 1920, 1988, 1992, 1996, 2020, 2024, 2096
        ]
        for year in leap_years:
            # SubTest helps isolate failures for each year
            with self.subTest(year=year):
                self.assertTrue(leapyear.to_leap_year(year), f"{year} should be a leap year")

    # Test a list of known non-leap years
    def test_non_leap_years_in_range(self):
        # Years that are not leap years
        non_leap_years = [
            1, 2, 3, 100, 200, 300, 1700, 1800, 1900, 2100, 2021, 2022, 2023, 2025, 2099
        ]
        for year in non_leap_years:
            # SubTest helps isolate failures for each year
            with self.subTest(year=year):
                self.assertFalse(leapyear.to_leap_year(year), f"{year} should not be a leap year")

# Run the unit tests with more detailed output
if __name__ == '__main__': # pragma: no cover
    unittest.main(verbosity=2)