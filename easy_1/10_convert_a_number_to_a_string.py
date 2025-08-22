"""
In the previous two exercises, you developed functions that convert simple 
numeric strings to signed integers. In this exercise and the next, you're going
to reverse those functions.

Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, 
and so on) to the string representation of that integer.

You may not use any of the standard conversion functions available in Python, 
such as `str`. Your function should do this the old-fashioned way and construct
the string by analyzing and manipulating the number.
"""
"""
I: an integer
O: the string version of that integer

Rules:
- input will be non-negative
- may not use standard conversion built-in functions
- hint: 
    - work through digits going right to left
    - divmod() will be helpful to extract each digit

Breakdown:
- a list of strings as hash map (the form of the remainder will 
  already be in integer form, so we can use them as the index)
- an empty string to build result upon
- divmod(dividend, divisor)
- divmod(4321, 10) gets us (432, 1)
- divmod(432, 10) gets us (43, 2) 
...
- divmod(4, 10) gets us (0, 4)
- tuple unpacking to assign `dividend` & `remainder`
- match `remainder` to DIGITS
- concatenate backwards -> remainder + str_num

Algo:
- create a list of string digits `DIGITS` (outside function)
Inside function:

- initialize empty string `str_num`
- if num is 0:
    - return "0"

- loop while `num` is greater than 0:
    - assign result of divmod(num, 10) to num & remainder
    - get string equivalent of DIGITS[remainder]
    - concatenate result to str_num (assign back to str_num)

- return str_num

Step-through:
condition to stop looping: num > 0

input: 432

num: 432, 43, 4, 0
str_num: '', '2', '23', '423'
remainder: 2, 3, 4
(Loop tries to run again once num becomes 0, but the condition is no longer
met so it stops the next iteration.)

input: 0
str_num: ''
remainder: 
"""
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def integer_to_string(num):
    if num == 0:
        return "0"

    str_num = ''

    while num > 0:
        num, remainder = divmod(num, 10) 
        str_num = DIGITS[remainder] + str_num

    return str_num

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

# LS Solution
def integer_to_string(number):
    DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result
    
    return result or "0"

"""
The last line, `return result or "0"` works by returning `result` if it is a
truthy value, or if it is falsy (an empty string), it returns `"0"`.

This is because the `or` operator returns the first truthy value it encounters
or if both are falsy, returns the last evaluated value.
"""
