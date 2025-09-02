"""
Write a function that takes a string, doubles every character in the string, 
then returns the result as a new string.
"""
"""
I: a string
O: a new string, with each character doubled

Breakdown:
- initialize doubled_str to an empty string
- Iterate through the string, and for each character:
    - multiply it by 2
    - concatenate it to doubled_str
- return doubled_str
"""
# Using string concatenation
def repeater(txt):
    doubled_str = ''

    for char in txt:
        doubled_str += char * 2

    return doubled_str

"""
Breakdown:
- initialize doubled_str to an empty list
- Iterate through the string, and for each character:
    - multiply it by 2
    - append it to doubled_str
- join substrings in doubled_str together & return it
"""
# Using a list comprehension
def repeater(txt):
    return ''.join([char * 2 for char in txt])

# Using a generator expression
def repeater(txt):
    return ''.join(char * 2 for char in txt)

"""
The generator expression is more memory-friendly.
"""

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
