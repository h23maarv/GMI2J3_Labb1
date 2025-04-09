# Importing the unittest module to write unit tests
# and importing the roman10 module which contains the functions to be tested
import unittest
import roman10

# Test class that tests known correct conversions between integers and Roman numerals
class KnownValues(unittest.TestCase):
    # List of known value pairs (integer <-> Roman numeral)
    known_values = (
        (1, 'I'), (2, 'II'), (3, 'III'),
        (4, 'IV'), (5, 'V'), (6, 'VI'),
        (7, 'VII'), (8, 'VIII'), (9, 'IX'),
        (10, 'X'), (31, 'XXXI'), (40, 'XL'), (50, 'L'), (90, 'XC'),
        (100, 'C'), (400, 'CD'), (500, 'D'), (1000, 'M'),
        (148, 'CXLVIII'), (294, 'CCXCIV'), (312, 'CCCXII'),
        (421, 'CDXXI'), (528, 'DXXVIII'), (621, 'DCXXI'),
        (782, 'DCCLXXXII'), (870, 'DCCCLXX'), (900, 'CM'), (941, 'CMXLI'),
        (1043, 'MXLIII'), (1110, 'MCX'), (1226, 'MCCXXVI'),
        (1301, 'MCCCI'), (1485, 'MCDLXXXV'), (1509, 'MDIX'),
        (1607, 'MDCVII'), (1754, 'MDCCLIV'), (1832, 'MDCCCXXXII'),
        (1993, 'MCMXCIII'), (2074, 'MMLXXIV'), (2152, 'MMCLII'),
        (2212, 'MMCCXII'), (2343, 'MMCCCXLIII'), (2499, 'MMCDXCIX'),
        (2574, 'MMDLXXIV'), (2646, 'MMDCXLVI'), (2723, 'MMDCCXXIII'),
        (2892, 'MMDCCCXCII'), (2975, 'MMCMLXXV'), (3051, 'MMMLI'),
        (3185, 'MMMCLXXXV'), (3250, 'MMMCCL'), (3313, 'MMMCCCXIII'),
        (3408, 'MMMCDVIII'), (3501, 'MMMDI'), (3610, 'MMMDCX'),
        (3743, 'MMMDCCXLIII'), (3844, 'MMMDCCCXLIV'), (3888, 'MMMDCCCLXXXVIII'),
        (3940, 'MMMCMXL'), (3999, 'MMMCMXCIX')
    )


    # Tests that to_roman() returns the correct Roman numeral for each integer
    def test_to_known_values(self):
        for integer, numeral in self.known_values:
            self.assertEqual(roman10.to_roman(integer), numeral)

    # Tests that from_roman() returns the correct integer for each Roman numeral
    def test_from_known_values(self):
        for integer, numeral in self.known_values:
            self.assertEqual(roman10.from_roman(numeral), integer)

    # Tests round-trip conversion (integer -> Roman -> integer) for the full range 1–3999
    def test_roundtrip(self):
        for integer in range(1, 4000):
            numeral = roman10.to_roman(integer)
            result = roman10.from_roman(numeral)
            self.assertEqual(integer, result)

# Test class that checks invalid inputs for to_roman()
class ToRomanBadInput(unittest.TestCase):
    # Tests that numbers greater than 4999 raise OutOfRangeError
    def test_too_large(self):
        with self.assertRaises(roman10.OutOfRangeError):
            roman10.to_roman(5000)

    # Tests that 0 raises OutOfRangeError (Roman numerals have no representation for 0)
    def test_zero(self):
        with self.assertRaises(roman10.OutOfRangeError):
            roman10.to_roman(0)

    # Tests that negative numbers are not allowed
    def test_negative(self):
        with self.assertRaises(roman10.OutOfRangeError):
            roman10.to_roman(-1)

    # Tests that floating point numbers raise NotIntegerError
    def test_non_integer(self):
        with self.assertRaises(roman10.NotIntegerError):
            roman10.to_roman(0.5)

    # Custom test case: Tests that a string input raises NotIntegerError
    def test_with_string_input(self):
        with self.assertRaises(roman10.NotIntegerError):
            roman10.to_roman("10")

    # Custom test case: Tests that the highest valid number (4999) is converted correctly
    def test_edge_high(self):
        self.assertEqual(roman10.to_roman(4999), "MMMMCMXCIX")

# Test class that checks invalid inputs for from_roman()
class FromRomanBadInput(unittest.TestCase):
    # Tests that an empty string is not allowed
    def test_blank(self):
        with self.assertRaises(roman10.InvalidRomanNumeralError):
            roman10.from_roman('')

    # Tests that a completely invalid string raises an error
    def test_invalid_string(self):
        with self.assertRaises(roman10.InvalidRomanNumeralError):
            roman10.from_roman('ZZZ')

    # Custom test case: Tests that lowercase letters are not allowed
    def test_from_roman_with_lowercase(self):
        with self.assertRaises(roman10.InvalidRomanNumeralError):
            roman10.from_roman("x")

    # Custom test case: Tests that invalid types raise an error
    def test_from_roman_with_non_string_input(self):
        invalid_inputs = [123, 4.5, None, [], True]
        for invalid_input in invalid_inputs:
            with self.assertRaises(roman10.InvalidRomanNumeralError):
                roman10.from_roman(invalid_input)

    # Custom test case: Tests invalid subtractive combinations
    def test_from_roman_invalid_subtractive_pair(self):
        with self.assertRaises(roman10.InvalidRomanNumeralError):
            roman10.from_roman("IC")