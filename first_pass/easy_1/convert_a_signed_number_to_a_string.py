"""
I: an integer - neg/pos/zero
O: a string version of the input integer

✱ RULES ✱
- solution: a function that converts a pos or neg integer value to the string
  representation of that integer.
- if the input is zero, a string version of zero must be returned.
- standard conversion functions such as `str()` cannot be used.
- hint: easiest approach is to work through the digits of each number, from
  right-to-left. The `divmod()` function may be helpful to extract each digit.
- The `integer_to_string()` function from the previous exercise can be used.

✱ EXAMPLES / TEST CASES ✱
- 4321 -> "+4321"
- -123 -> "-123"
- 0 -> "0"

✱ QUESTIONS ✱
- what is the range of numbers we're working with?
    + 0 
    + negative numbers
    + positive numbers (per rules)
- what is the `divmod()` function?
    + it takes two numbers and returns a tuple containing the quotient and the
      remainder when argument1 (the dividend) is divided by argument2 (the 
      divisor).
- how do i differentiate between negative numbers and positive numbers?
    + whether a number is bigger than 0 or smaller than 0
    - what about zero?
        + it's neither pos or neg, so gotta handle that one on its own
- will a negative number make a difference in matching the string versions?
    + the `integer_to_string()` function does not handle negative numbers -
      so the argument passed to it has to be positive
    + but it handles positive numbers as well as zero.

✱ DS ✱
- an empty string to concatenate a '+' or a '-'

✱ ALGORITHM ✱
I: `num`
[x] get the absolute value of num, assign to `positive_num`
[x] call integer_to_string(positive_num) function - assign returning value to
   `string_digits`
[x] if `num` is negative (less than 0):
    [] concatenate '-' to string_digits and return it
[x] else if `num` is positive (more than 0):
    [] concatenate '+' to string_digits and return it
[x] else: 
    [] return string_digits
"""
def integer_to_string(num):
    DIGITS = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9"
    }
    result = ''

    if num:
        while num > 0:
            num, remainder = divmod(num, 10)
            result += DIGITS[remainder]
        return result[::-1]
    else:
        return DIGITS[num]

def signed_integer_to_string(num):
    positive_num = abs(num)

    string_digits = integer_to_string(positive_num)

    if num < 0:
        return '-' + string_digits
    elif num > 0:
        return '+' + string_digits
    else:
        return string_digits


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

# LS Solution
def signed_integer_to_string(number):
    if number < 0:
        return f"-{integer_to_string(-number)}"
    elif number > 0:
        return f"+{integer_to_string(number)}"
    else:
        return "0"
