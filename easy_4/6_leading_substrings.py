"""
Write a function that takes a string argument and returns a list of substrings 
of that string. Each substring should begin with the first letter of the word, 
and the list should be ordered from shortest to longest.
"""
"""
I: a str
O: a list, of substrings

Ex:
- 'a' ==> ['a']
- 'abc' ==> ['a', 'ab', 'abc']
- 'xyzy' ==> ['x', 'xy', 'xyz', 'xyzy']

Rules:
- each subsequent substring in the output list increases by 1 letter
- the list is "finished" when the entire input string is included at the
  end of the list

DS/Brainstorm:
- grow the substring one by one, keeping track of it via a variable
- iterate through each character in input string
    - use the fact that it moves up a char each loop -> to grow the substring
    - save its state to growing_str each loop

Algo:
    - SET `substr_list` to an empty list
    - SET `growing_str` to an empty string
    - for each character in the input string:
        - concatenate that character to `growing_str`
            - NOTE REASSIGN to `growing_str`
        - append `growing_str` to `substr_list`
    - return `substr_list`
"""
def leading_substrings(txt):
    substr_list = []
    growing_str = ''

    for char in txt:
        growing_str = growing_str + char
        substr_list.append(growing_str)

    return substr_list

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
