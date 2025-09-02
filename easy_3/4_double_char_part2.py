"""
Write a function that takes a string, doubles every consonant in the string, 
and returns the result as a new string. The function should not double vowels 
('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.
"""
"""
I: a string
O: a new string with every consonant in input string doubled

Rules:
- vowels, digits, punctuation, whitespace should be skipped

Breakdown:
- set CONSONANTS to 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
- iterate through the string, and for each character:
    - if it exists in CONSONANTS:
        - add char * 2 to list
    - else:
        - add char to list
- join substrings together and return it
"""
CONSONANTS = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

# Using a list
def double_consonants(txt):
    doubled_cons = []

    for char in txt:
        if char in CONSONANTS:
            doubled_cons.append(char * 2)
        else:
            doubled_cons.append(char)

    return ''.join(doubled_cons)

# Using a ternary expression in a generator expression
def double_consonants(txt):
    return ''.join((char * 2 if char in CONSONANTS else char) for char in txt)

# Using string concatenation
def double_consonants(txt):
    doubled_cons = ''

    for char in txt:
        if char in CONSONANTS:
            doubled_cons += char * 2
        else:
            doubled_cons += char

    return doubled_cons

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
