"""
Write another function that returns `True` if the string passed as an argument 
is a palindrome, or `False` otherwise. This time, however, your function should 
be case-insensitive, and should ignore all non-alphanumeric characters. If you 
wish, you may simplify things by calling the `is_palindrome` function you wrote 
in the previous exercise.
"""
"""
Ex:
- "Madam, I'm Adam" => True
    - now the ' doesn't matter

Rules:
- function is case-insensitive
- all non-alphanumeric characters should be ignored
- can use the function from previous exercise

Breakdown:
- convert to lowercase
- "clean" the string by putting together another form without the punctuation
- pass that "cleaned" string to the is_palindrome function

Algo:
- SET cleaned_str = ''
- iterate through txt - for each character:
    - check if the character is alphanumeric
        - if it is:
            - concatentate the lowercase version of it to cleaned_str
- return the result of calling the is_palindrome function with cleaned_str as
  the argument
"""
def is_palindrome(txt):
    return txt == txt[::-1]

def is_real_palindrome(txt):
    cleaned_str = ''
    for char in txt:
        if char.isalnum():
            cleaned_str += char.casefold()
    return is_palindrome(cleaned_str)

# REFACTORED VERSION
def is_real_palindrome(txt):
    cleaned_str = ''.join(char.casefold() for char in txt if char.isalnum())
    return is_palindrome(cleaned_str)

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

