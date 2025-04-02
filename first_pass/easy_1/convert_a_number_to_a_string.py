"""
I: a non-negative integer
O: a string version of the input integer

✱ QUESTIONS ✱
- what is the range of numbers we're working with?
    + 0 and positive numbers (per rules)
- what is the `divmod()` function?
    + it takes two numbers and returns a tuple containing the quotient and the
      remainder when argument1 (the dividend) is divided by argument2 (the 
      divisor).

✱ RULES ✱
- solution: a function that converts a non-negative integer value to the string
  representation of that integer.
- standard conversion functions such as `str()` cannot be used.
- hint: easiest approach is to work through the digits of each number, from
  right-to-left. The `divmod()` function may be helpful to extract each digit.

✱ EXAMPLES / TEST CASES ✱
- 4321 -> "4321"
- 0 -> "0"
- 5000 -> "5000"
- 1234567890 -> "1234567890"

✱ DS ✱
- an empty string to collect the digits 
- a dictionary mapping numbers with their string counterparts

✱ ALGORITHM ✱
I: `num`
[x] initialize dictionary of digits/string digits `DIGITS`
[x] initialize empty string `result`'
[x] while num is bigger than 0:
    [x] get the quotient and the remainder of num in a tuple (divmod())
    [x] extract the quotient and reassign to `num`
    [x] extract the remainder and assign to `remainder`
    [x] get the string counterpart of the remainder, concatenate it to result
[x] return result

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

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True


# LS SOLUTION
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number):
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    return result or '0'
