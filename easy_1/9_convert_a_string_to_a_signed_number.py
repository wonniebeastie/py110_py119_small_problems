"""
In the previous exercise, you developed a function that converts simple numeric
strings to integers. In this exercise, you're going to extend that function to
work with signed numbers.

Write a function that takes a string of digits and returns the appropriate 
number as an integer. The string may have a leading `+` or `-` sign; if the 
first character is a `+`, your function should return a positive number; if it 
is a `-`, your function should return a negative number. If there is no sign, 
return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python, 
such as `int`. You may, however, use the `string_to_integer` function from the 
previous exercise.
"""
"""
I: a string of digits led by "+" or "-" or no sign
O: an integer form of the input

Rules:
- cannot use built-in standard conversion functions
- function should calculate result using characters in input string
- if string leads with

Breakdown:
- previous function converts the number for us already
- slicing for dealing with leading signs
- unary negation operator to deal with negative sign

Algo:
- if `str_digits` leads with "-":
    - call `string_to_integer()` using just the number part of str_digits 
      ([1:])
    - use `-` operator to turn it into a negative number
    - return it
- else if it leads with "+":
    - call `string_to_integer()` using just the number part of str_digits 
      ([1:])
    - return the result
- else:
    - return result of `string_to_integer()` using str_digits the argument
"""
def string_to_integer(str_digits):
    DIGITS = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    total = 0
    for digit in str_digits:
        total = (10 * total) + DIGITS[digit] 
    return total

def string_to_signed_integer(str_digits):
    if str_digits.startswith("-"):
        return -string_to_integer(str_digits[1:])
    elif str_digits.startswith("+"):
        return string_to_integer(str_digits[1:])
    else:
        return string_to_integer(str_digits)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
