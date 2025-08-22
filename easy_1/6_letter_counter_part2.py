"""
Modify the word_sizes function from the previous exercise to exclude non-
letters when determining word size. For instance, the word size of "it's" is 3,
not 4.
"""
"""
I: a string of words
O: a dictionary of counts of words

Ex:
- "What's up doc?" => {5: 1, 2: 1, 3: 1}
    - What's = 5
    - up = 2
    - doc = 3
    - each appear once

Rules:
- exclude non-letters in count for the word length this time

Breakdown:
- use a helper function to "clean" the input string
- this would 

-- HELPER (clean_word) --
I: input string
O: a new string without the non-letters

Goal:
To produce a new string

Algo:
- initialize an empty string `cleaned_str`
- iterate through input string
    - for each letter, check if it's a letter or a space:
        - if it is a letter or a space:
            - concatenate it to cleaned_str
- return cleaned_str
"""
# FIRST APPROACH
def clean_str(sentence):
    cleaned_str = ''

    for char in sentence:
        if char.isalpha() or char.isspace():
            cleaned_str += char

    return cleaned_str

def word_sizes(sentence):
    cleaned_sentence = clean_str(sentence)
    counts = {}

    for word in cleaned_sentence.split():
        counts[len(word)] = counts.get(len(word), 0) + 1

    return counts

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1}) # True

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3}) # True

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1}) # True

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1}) # True

print(word_sizes('') == {}) # True

"""
My initial way was to re-build the input string without non-letter characters
and then do the same thing as the last problem, split it into a list of words
and then build a frequency map of the counts.
"""

# SECOND APPROACH
def word_sizes(txt):
    len_counts = {}
    for word in txt.split():
        clean_word = ''.join(char for char in word if char.isalpha())
        len_counts[len(clean_word)] = len_counts.get(len(clean_word), 0) + 1

    return len_counts

"""
This code also works, but here we're cleaning each word separately, instead of
cleaning the entire string once like in the first approach. We also use a 
generator expression instead of concatenation to join the strings together,
which makes this approach more concise/efficient.

This approach might be better for shorter strings, but the first approach of
cleaning the entire string once at the beginning might be better for very large
inputs.
"""
