"""
Given a string of words separated by spaces, write a function that swaps the 
first and last letters of every word.

You may assume that every word contains at least one letter, and that the 
string will always contain at least one word. You may also assume that each 
string contains nothing but words and spaces, and that there are no leading, 
trailing, or repeated spaces.
"""
"""
I: a string
O: a new string, each word having the first & last letters swapped

Ex:
- 'Abcde' => "ebcdA"
    - A & e

Rules:
- each word will have at least one letter
- each string will have at least one word
- each string will only have words & spaces,
    - no leading, trailing, or repeated spaces

Breakdown:
- split into list of words
- swap each word's first and last letters
- join them into a new string and return it

Algo:
- if the length of input string is 1:
    - return it as is
- split input string into a list of words
- iterate through each word in word_list:
    - call swap_letters() on each word
- join the swapped words together into a single string and return it

-- HELPER (`swap_letters()`) --
I: a word
O: the input word, but with first & last letters swapped

Algo:
- if length of word is 1:
    - return it as is
- concatenate last letter (word[-1]) with the middle part of the word 
  (word[1:-1]) with the first letter (word[0])
- return the concatenated word
"""
def swap_letters(word):
    if len(word) == 1:
        return word

    return word[-1] + word[1:-1] + word[0]

def swap(txt):
    return ' '.join(swap_letters(word) for word in txt.split())

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
