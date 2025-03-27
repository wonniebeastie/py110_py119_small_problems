"""
I: a string
O: a string, with the first and last letters of every word swapped

✱ QUESTIONS ✱
- what if the input string is empty?
    + every word contains at least one letter (rules)
- what if the input string has special characters?
    + each string always includes only words and spaces (rules)
- what if the input string only has one letter?
    + the output will be the same as input (per example)
- What if the input string has more than one word? 
    + the swap applies to each individual word (per example)
- Is case important?
    + case should stay the same regardless of swap (per example)
- What if there are multiple spaces?
    + no repeated spaces (rules)

✱ RULES ✱
- solution: as a function
- every word contains at least one letter
- each string:
    - contains at least one word
    - contains nothing but words and spaces
- no leading/trailing/repeated spaces

✱ EXAMPLES / TEST CASES ✱
- 'Oh what a wonderful day it is' -> "hO thaw a londerfuw yad ti si"
- Abcde' -> "ebcdA"
- 'a' -> "a"

✱ DS ✱
- a list that contains the words separated individually.
- a helper function that swaps the first and last letters and returns it:
    - a list to contain the individual letters
- a new list that contains the transformed words.

✱ ALGORITHM ✱
I: `txt`
[] separate words in txt by white space into a list - assign to `words_list`
[] create a new list from collection words_list - assign to `swapped_words_list`
	[] for each word:
		transform: call `swap_first_last_letters()` helper function 
[x] join the words in swapped_words_list together with a space in between each 
    word & return it as a single string.
"""
def swap(txt):
    words_list = txt.split()

    swapped_words_list = [swap_first_last_letters(word) for word in words_list]

    return ' '.join(swapped_words_list)


"""
<-------- HELPER FUNCTION:  -------->
I: a string (a word)
O: a string (input word with first and last letters swapped places)

✱ DS / VIS ✱
- a list that contains the individual letters

✱ ALGO ✱
I: `word`
[] if length of word is 1:
    return word
[x] return the last letter of word concatenated with the middle letters and the 
   first letter 
<------------------------------>
"""
def swap_first_last_letters(word):
    if len(word) == 1:
        return word

    return word[-1] + word[1:-1] + word[0]

print(swap_first_last_letters('what')) # thaw

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
