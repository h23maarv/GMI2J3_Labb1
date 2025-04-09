import re
# Custom exception classes used to signal specific errors
# These inherit from ValueError and are used for testable and clear error handling
class OutOfRangeError(ValueError): pass      # For values outside the range 1–4999
class NotIntegerError(ValueError): pass      # For non-integer values
class InvalidRomanNumeralError(ValueError): pass  # For invalid Roman numerals

# Regular expression to validate Roman numerals from 1 to 3999
roman_numeral_pattern = re.compile('''^     # beginning of string
    M{0,3}                                  # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})                        # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs), # or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})                        # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs), # or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})                        # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is), # or 5-8 (V, followed by 0 to 3 Is)
    $                                       # end of string''',
    re.VERBOSE)             # Allows whitespace and comments in regex

# A tuple defining the mapping between Roman characters and their integer values
# Used for conversion from integer to Roman numeral
roman_numeral_map = (
    ('M',  1000), ('CM', 900), ('D',  500), ('CD', 400),
    ('C',  100),  ('XC', 90),  ('L',  50),  ('XL', 40),
    ('X',  10),   ('IX', 9),   ('V',  5),   ('IV', 4),
    ('I',  1)
)

# Precomputed lookup tables for fast conversions
to_roman_table = [None]                 # Index = integer, value = Roman numeral
from_roman_table = {}                   # Key = Roman numeral, value = integer
valid_roman_letters = set("MDCLXVI")    # Valid Roman characters

# Function to convert an integer to a Roman numeral
def to_roman(n):
    '''Converts integer to Roman numeral'''
    if not isinstance(n, int):  # Ensure input is an integer
        raise NotIntegerError('non-integers can not be converted')
    if not (0 < n < 5000):      # Restriction according to traditional Roman system
        raise OutOfRangeError('number out of range (must be 1..4999)')
    return to_roman_table[n]    # Return the corresponding Roman numeral

# Function to convert a Roman numeral to an integer
def from_roman(s):
    '''Converts Roman numeral to integer'''
    if not isinstance(s, str):      # Input must be a string
        raise InvalidRomanNumeralError('Input must be a string')
    if not s:                       # String must not be empty
        raise InvalidRomanNumeralError('Input can not be blank')
    if any(char not in valid_roman_letters for char in s): # Check for invalid characters
        raise InvalidRomanNumeralError("Invalid characters in input")
    if s not in from_roman_table:   # Validate the Roman numeral
        raise InvalidRomanNumeralError(f'{s} is not a valid Roman numeral')
    return from_roman_table[s]      # Return the corresponding integer

# Builds the lookup tables for fast conversions between integers and Roman numerals
def build_lookup_tables():
    def build(n):
        result = ''
        for numeral, integer in roman_numeral_map:
            if n >= integer:
                result = numeral       # Add the first matching Roman symbol
                n -= integer
                break                  # Stop so the remainder is handled recursively
        if n > 0:
            result += to_roman_table[n]  # Add the rest using previously computed value
        return result

    # Build tables for all values 1–4999
    for integer in range(1, 5000):
        roman = build(integer)
        to_roman_table.append(roman)
        from_roman_table[roman] = integer

# Run the table-building function so they are ready before conversion is used
build_lookup_tables()