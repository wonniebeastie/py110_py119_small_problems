"""
I: a string
O: a dictionary that shows the number of words of different sizes

✱ QUESTIONS ✱
- What is a word?
    + A word is any sequence of letters that are separated by spaces.
    + Examples: 
        + "Four" (4 letters)
        + "What's" (5 letters)
        + "w@ll" (3 letters)
- What about empty strings?
    + They will return an empty dictionary.
- What if there is more than one space between the words?
    + Directions say "consisting of zero or more space-separated words" so the
      number of spaces does not affect the output.
- What if the string only has punctuation instead of letters?

✱ RULES ✱
- solution must be in the form of a function
- spaces mark the end of words
- dictionary key must be the length of the word
    + punctuation does NOT count towards word length.
        - must be ignored.
    + the value must be the number of times it occurs in the string.
- the key & value order follows the word order in the input string, not in any
  ascending or descending order.
- if the input string is empty, the output dictionary must also be empty.

✱ EXAMPLES / TEST CASES ✱
- 'Four score and seven.' -> {4: 1, 5: 2, 3: 1}
- "What's up doc?" -> {5: 1, 2: 1, 3: 1}
- '' -> {}
Own test cases:
- 'hello   clouds!' -> {4: 1, 6: 1}
- '!!!' -> {}
- '!!! hello ~ wow .' -> {5: 1, 3: 1}

✱ DS ✱
- A list of the words in the input string.
- An empty dictionary to collect the counts.
- A new list to add the new words without punctuation.
- An empty string to concatenate each letter to, to form the words without
  punctuation.

✱ ALGORITHM ✱
I: `txt`
[] Initialize empty dictionary - `letter_count`
[] Initialize a list of the words in `txt`, using spaces as the separator 
   between words - assign to `words_list`.

[x] create a list of words without punctuation - `new_words_list`
    - from: `words_list`
    - filter for: n/a
    - do what: call `form_new_word()` function

[] For each `word` in `new_words_list`:
    [] Count the number of characters in `word` - assign to `length`
        [] If this number does not already exist in `letter_count`:
            [] Add a new key-value pair to `letter_count` - 
                using `length` as the key, and 0 as the value.
        [] Increment value of the `length` key by 1.

[] Return `result`
"""

def word_sizes(txt):
    letter_count = {}
    words_list = txt.split()

    new_words_list = [form_new_word(word) for word in words_list]

    for word in new_words_list:
        length = len(word)

        if length == 0:
            continue

        if length not in letter_count:
            letter_count[length] = 0

        letter_count[length] += 1

    return letter_count

"""
<-------- HELPER FUNCTION: `form_new_word()` -------->
PURPOSE
To return a word without puntuation. 

I: a string (a word) - `word`
O: a string, the input string without punctuation

✱ DS / VIS ✱
- An empty string for form new word without punctuation.

✱ ALGO ✱
[] Initialize empty string - `new_word`.

[] For each `letter` in each `word`:
    [] Check if the `letter` is a letter.
        [] If it is, concatenate `letter` to `new_word`.

[x] Return `new_word`
<------------------------------>
"""
def form_new_word(word):
    new_word = ''

    for letter in word:
        if letter.isalpha():
            new_word += letter

    return new_word

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

print(word_sizes('!!!'))
print(word_sizes('!!! hello ~ wow .'))
