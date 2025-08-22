"""
Write a function that returns `True` if the string passed as an argument is a 
palindrome, `False` otherwise. A palindrome reads the same forwards and 
backwards. For this problem, the case matters and all characters matter.
"""
"""
I: a string
O: a boolean

Ex:
- "madam i'm adam" => False
    - punctuation
- 'Madam' => False
    - M is uppercase while m is not

Rules:
- function should return True if palindrome
- False otherwise
- case matters
- all characters
- a palindrome reads the same forwards & backwards

Breakdown:
- compare the input string to its reverse
"""
def is_palindrome(txt):
    return txt == txt[::-1]

# All of these examples should print True
print(is_palindrome('madam') == True) # True
print(is_palindrome('356653') == True) # True
print(is_palindrome('356635') == False) # True

# case matters
print(is_palindrome('Madam') == False) # True

# all characters matter
print(is_palindrome("madam i'm adam") == False) # True
