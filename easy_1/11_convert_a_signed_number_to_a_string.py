"""
In the previous exercise, you developed a function that converts non-negative 
numbers to strings. In this exercise, you're going to extend that function by 
adding the ability to represent negative numbers as well.

Write a function that takes an integer and converts it to a string 
representation.

You may not use any of the standard conversion functions available in Python, 
such as `str`. You may, however, use `integer_to_string` from the previous 
exercise.
"""
"""
I: an integer
O: the string version of integer

Rules:
- if input is a positive number, add "+" to the beginning of the string
- if the input is a negative number, add "-" to beginning
- if input is 0, just return "0"

Breakdown:
- check if num is 0, bigger than 0 or larger than 0
- if number is negative, pass to function the positive version of it
    - `-` unary negation operator to negate it to positive

Algo:
- if number is greater than 0:
    - concatenate "+" to result of integer_to_string(number)
    - return it
- else if number is less than 0:
    - concatenate "-" to result of integer_to_string(-number)
    - return it
- else:
    - return integer_to_string(number)
"""
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def integer_to_string(number):
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result
    
    return result or "0"

def signed_integer_to_string(number):
    if number > 0:
        return "+" + integer_to_string(number)
    elif number < 0:
        return "-" + integer_to_string(-number)
    else:
        return "0"

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
