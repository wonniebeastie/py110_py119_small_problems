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
- comprehension
- loop through indices of txt
- grow a slice that starts from index 0 & ends at index + 1

Algo:
    - iterate through all of txt, keeping track of index:
        - use slicing to add a slice of txt each loop
            NOTE (starting from 0 & ending in index + 1)
"""
def leading_substrings(txt):
    return [txt[:idx + 1] for idx in range(len(txt))]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
