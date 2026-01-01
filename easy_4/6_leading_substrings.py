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
- Keep track of index & current slice in the loop, add current slice to
  the output list, increment the index, until the end is reached.

Algo:
    - SET idx to 1
    - SET substrings_list to an empty list
    - while the index is not equal to the end of the length of the string + 1:
        - SET current_slice to txt[:idx]
        - increment idx by 1
    - return substrings_list
"""
def leading_substrings(txt):
    idx = 1
    substrings_list = []

    while idx != len(txt) + 1:
        current_slice = txt[:idx]
        idx += 1
        substrings_list.append(current_slice)

    return substrings_list

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
