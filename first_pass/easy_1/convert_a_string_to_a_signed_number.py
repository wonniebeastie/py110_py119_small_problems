"""
✱ ALGORITHM ✱
I: `string`
[] if the first character of string is "-":
    call string_to_integer and pass in string but without the first character
    return value (preceded by `-`)
[] else if the first character of string is "+":
    call string_to_integer and pass in num_string but without the first character
    return value
[] else:
    call string_to_integer(string)
    return value
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

def string_to_signed_integer(string):
    if string[0] == '-':
        return -string_to_integer(string[1:])
    elif string[0] == '+':
        return string_to_integer(string[1:])
    else:
        string_to_integer(string)

string_to_signed_integer("-4321")
