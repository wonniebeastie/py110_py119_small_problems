"""
Write a function that takes a string of digits and returns the appropriate 
number as an integer. You may not use any of the standard conversion functions 
available in Python, such as `int`. Your function should calculate the result 
by using the characters in the string.

For now, do not worry about leading `+` or `-` signs, nor should you worry 
about invalid characters; assume all characters are numeric.
"""
"""
I: a string of digits
O: an integer form of the input

Rules:
- cannot use built-in standard conversion functions
- function should calculate result using characters in input string
- assume all characters are numeric

Breakdown:
- a digit's place == how many groups of 10 it represents:
    - starting with ones on the right
    - increasing tenfold for each position left
    - ex: 573
        - 3 groups of 1s (3 x 1 = 3)
        - 7 groups of 10s (7 x 10 = 70)
        - 5 groups of 100s (5 x 100 = 500)
        - add them together and it's 573
- map string digits to integers using a dictionary
- use a `total` variable that starts as 0 (value of the digits processed so far)
- iterate through input string, and for each digit:
    - multiply each digit in string by 10 to "shift" it one digit to the left
    - look up number value of string digit
    - add it to total 

Algo:
- Create a dictionary to map string digits to numbers (`DIGITS`)
- Start `total` at `0`
- For each `digit` in `str_digits`:
    - Take the current total and multiply it by `10`
    - Add the returning value of DIGITS[digit] to `total`
- return `total`
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

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

# SECOND APPROACH
def string_to_integer(str_num):
    NUMBERS = {
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
    ZEROS = {
        0: 1,
        1: 10,
        2: 100,
        3: 1000,
    }
    result = []

    for idx in range(len(str_num)):
        digit = NUMBERS.get(str_num[idx])
        if len(str_num[idx+1:]) > -1:
            multiplier = ZEROS.get(len(str_num[idx+1:]))
        result.append(digit * multiplier)

    return sum(result)

"""
The more convoluted way I initially solved it. It calculates and stores each
digit's full place value separately. It's not as readable and uses extra memory
to store intermediate results/adds more steps.
"""
