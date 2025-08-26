"""
Write a function that takes a list of positive integers as input, multiplies 
all of the integers together, divides the result by the number of entries in 
the list, and returns the result as a string with the value rounded to three 
decimal places.
"""
"""
I: a list of numbers
O: a string, value rounded to 3 decimal places

Rules:
- multiply all integers
- divide the result by length of input iterable
- convert result into a string

Breakdown:
- helper function to multiply numbers
- divide by length 
- convert it into a string, decimal to 3 places

-- HELPER --> `multiply_nums()`
I: the input list
O: the result of multiplying all numbers together
- product = 1
- iterate through input list, and for each number:
    - multiply it with product, assign it back to product
- return product
"""
def multiplicative_average(numbers):
    result = multiply_nums(numbers) / len(numbers)
    return f"{result:.3f}"

def multiply_nums(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

"""
MANUAL OPTION (for 3 decimal places):
-- FROM MAIN -->
- after converting the result to a string
- call round_to_3(result), return the result

-- HELPER --> `round_to_3()`
I: the result, as a string
O: the result, either padded with zeros or cut to 3 decimal places

Helper Algo:
- if the length of digits[1] is less than 3:
    - split result into a list of digits, using "." as the delimiter `digits`
    - initialize `digit_len` with length of digits[1]
    - while digit_len is less than 3:
        - concatenate "0" to digits[1] & assign it back to digits[1]
        - get the length of digits[1] again & assign it back to digit_len
    - join `digits` list back up using "." as the delimiter and return it
- else:
    - turn str_result back into a float
    - round it using `round()` function, with 3 as the number of decimal places
    - turn it back into a string & return it
"""
def multiplicative_average(numbers):
    result = multiply_nums(numbers) / len(numbers)
    return round_to_3(str(result))

def multiply_nums(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def round_to_3(str_result):
    digits = str_result.split('.')

    if len(digits[1]) < 3:
        digit_len = len(digits[1])
        while digit_len < 3:
            digits[1] += "0"
            digit_len = len(digits[1])
        return '.'.join(digits)
    else:
        return str(round(float(str_result), 3))
