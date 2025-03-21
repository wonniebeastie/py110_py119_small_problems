# Solution 2: Comparing input string to its reverse
"""
I: a string
O: True or False

✱ EXAMPLES ✱
- Ex 1
- I: 'madam'
- O: True

- Ex 2
- I:'356653'
- O: True

✱ QUESTIONS ✱
- What is a palindrome?
    It's a word that reads the same forwards or backwards.

✱ RULES ✱
- Solution must be a function.
- Must returtn True if input string is a palindrome, False otherwise.
- Case matters
- All characters should be taken into account.

✱ ALGORITHM ✱
I: `txt`
[x] - Reverse the input text and assign to `reversed_txt`.
[x] - Compare `txt` and `reversed_txt` and see if they're an exact match.
[x] - If they're a match, return True
[x] - Else, return False

"""
def is_palindrome(txt):
    reversed_txt = txt[::-1]
    return txt == reversed_txt

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

# Solution 2: Checking characters from both ends of input string
"""
I: a string
O: True or False

✱ ALGORITHM ✱
[x] - initialize `left` with 0
[x] - initialize `right` with the length of the string - 1

[] - while the left index is less than the right index:
    [] + if the character on the left side does not match the character on the
         right, return `False`.
    [] + increment `left` by 1
    [] + decrement `right` by 1

[] - return `True`
"""
def is_palindrome2(txt):
    left = 0
    right = len(txt) - 1

    while left < right:
        if txt[left] != txt[right]:
            return False
        left += 1
        right -= 1

    return True

print(f"Other solution: {is_palindrome2('madam')}") # True
print(f"Other solution: {is_palindrome2('356653')}") # True
print(f"Other solution: {is_palindrome2('356635')}") # False
print(f"Other solution: {is_palindrome2('Madam')}") # False
print(is_palindrome2("madam i'm adam")) # False
