# Lab Report – Software Testing

This lab consists of three parts:
1. Roman numeral converter (Python)
2. Leap year checker (Python)
3. Prime number tester (JavaScript)

Each part demonstrates the use of unit testing, input validation, refactoring and code quality practices.

---

# Part 1: Roman Numerals – `roman10.py` and `romantest1.py`

# Description:
- Converts integers to Roman numerals and vice versa.
- Lookup tables used for efficient mapping.
- Validation via exceptions: `OutOfRangeError`, `InvalidRomanNumeralError`, `NotIntegerError`.

# Files:
- `roman10.py` – Contains `to_roman()` and `from_roman()` functions.
- `romantest1.py` – Unit tests using `unittest`.
- `romanmenu.py` – A menu-based interface for user interaction.

# Unit Testing:
- Tested known values, roundtrip conversions and input validation.
- Includes test cases not covered in the original book (e.g. lowercase input, wrong types).
- All test cases are organized using `unittest.TestCase`.

# Coverage:
- Achieved 100% test coverage on both statements and branches using `coverage.py`.

---

# Part 2: Leap Year – `leapyear.py` and `test_leapyear.py`

# Description:
- Function `to_leap_year(year)` returns True or False.
- Handles all Gregorian calendar rules.
- Input validation includes type checking and bounds.

# Files:
- `leapyear.py` – Main logic.
- `test_leapyear.py` – Unit tests organized by validation and known year results.

# Unit Testing:
- Tests a wide range of years including leap/non-leap.
- Tests invalid types: string, float, None, list, etc.
- Makes use of `subTest()` for clean iteration.

# Coverage:
- Achieved 100% statement and branch coverage using `coverage.py`.

---

# Part 3: Prime Numbers – `prime-calc1s.js`

# Description:
- Class-based design using `Check4Prime`.
- Uses the Sieve of Eratosthenes to build a lookup table on page load.
- Input validated via `checkArgs()` before checking primality.

# Files:
- `prime-calc1s.js` – Main logic, tests and input handling.
- `prime-assert1.html` – User interface and test visualization.
- `assert.css` – Styling for PASS/FAIL test results.

# Features:
- Method `primeCheck(num)` looks up value in precomputed array.
- Method `checkArgs()` validates number type, bounds, argument count.
- Function `checkFromInput()` connects form input to backend logic.

# Unit Testing:
- 9 test cases covering:
  - Known primes
  - Known non-primes
  - Invalid inputs (negative, float, string, multiple args)
- Uses `assert()` and `try/catch` structure for test evaluation.

---

# 1.4 Lab Feedback

# a) Were the labs relevant and appropriate? What about the length?

Yes – all parts were relevant and clearly designed to build a solid foundation in test-driven development. Python parts were well-scoped and educational. The JavaScript part was more challenging because we never programmed in this language, but it gave valuable insights into how test logic differs across languages. Length was reasonable when spread out.

# b) What corrections and/or improvements do you suggest?

The Roman and Leap year tasks were very clear. The JavaScript part could benefit from a more guided example on using `assert()` and integrating testing with HTML. It wasn’t obvious at first how error handling should affect the PASS/FAIL output. Otherwise, the structure and expectations were well balanced.