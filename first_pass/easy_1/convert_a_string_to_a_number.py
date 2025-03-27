"""
I: a string of numbers
O: an integer version of the input string

✱ QUESTIONS ✱
- what if the input is just 0?

✱ RULES ✱
- solution: a function
- cannot use standard conversion functions like `int()`
- the characters in the string should be used to calculate the result
- the polarity of the numbers does not matter.
- do not worry about invalid numbers
- assume all characters are numeric
- hint says understanding decimal numbers is important here. Shows an example
  of calculating "5372" as 5000 + 300 + 70 + 2 (5372)

✱ EXAMPLES / TEST CASES ✱
- "4321" -> 4321
- "570" -> 570
- "0" -> 0

✱ DS ✱
- a dictionary of string number values and their integer counterparts.
- a list to hold the converted values (to be summed)
- Left-to-Right: a 0 to add values to

✱ ALGORITHM ✱
LEFT-TO-RIGHT
I: `string_numbers`
[] create a dictionary mapping string digits to their integer values - assign 
   to `conversion_values`
[] initialize variable `result` with 0
[] for each character in string_numbers:
    [] look up its integer value from conversion_values dictionary
    [] multiply current result by 10
    [] add the integer value of the current digit to the result
[x] return the result
"""
def string_to_integer(string_numbers):
    conversion_values = {
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

    result = 0

    for current_num in string_numbers:
        result = (10 * result) + conversion_values[current_num]

    return result

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
