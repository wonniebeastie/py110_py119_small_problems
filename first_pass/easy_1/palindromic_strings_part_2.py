"""
I: a string
O: True or False

✱ QUESTIONS ✱
- What is meant by non-alphanumeric? 
    + So things that are not numbers and letters, like `'` in the last example.

✱ RULES ✱
- solution should be written as a function
- case-insensitive
- ignore all non-alphanumeric characters
- function from part 1 can be reused

✱ DS ✱
- empty string to concatenate transformed string to

✱ ALGORITHM ✱
I: `txt`
[x] initialize `converted_txt` with an empty string
[x] for each character in `txt`:
    [x] check if the character is alphanumeric
        [x] if it is:
            [x] convert to lowercase
            [x] concatenate to `converted_txt`
[x] initialize `reversed_txt` with reversed version of `converted_txt`
[x] check if they match
    [x] if they match return True
    [x] else return False
"""
def is_palindrome(txt):
    reversed_txt = txt[::-1]
    return txt == reversed_txt

def is_real_palindrome(txt):
    converted_txt = ''

    for char in txt:
        if char.isalnum():
            converted_txt += char.lower()

    return is_palindrome(converted_txt)


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True
