# -*- coding: utf-8 -*-
'''
There is a leap year every year whose number is perfectly divisible by four -
except for years which are both divisible by 100 and not divisible by 400.
The second part of the rule effects century years.
For example; the century years 1600 and 2000 are leap years,
but the century years 1700, 1800, and 1900 are not.
'''

class LeapYearError(ValueError): pass # Base class for leap year-related errors.
class NotIntegerError(LeapYearError): pass # Raised when the year is not an integer.
class OutOfRangeError(LeapYearError): pass # Raised when the year is out of valid range.

def to_leap_year(year):
    # Determines if a given year is a leap year.
    if not isinstance(year, int):
        raise NotIntegerError('Year must be an integer')
    if year <= 0:
        raise OutOfRangeError('Year must be a positive integer greater than 0')

    # Leap year logic
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Leap year
            else:
                return False  # Not a leap year
        else:
            return True  # Leap year
    else:
        return False  # Not a leap year


if __name__ == '__main__': #pregma: no cover
    try:
        year = int(input("Enter a year: "))
        print(f"{year} is leap year? {to_leap_year(year)}")
    except LeapYearError as e:
        print(f"Error: {e}")