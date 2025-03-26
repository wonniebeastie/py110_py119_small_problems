"""
I: a string
O: a dictionary that shows the number of words of different sizes

✱ QUESTIONS ✱
- What is a word?
    + A word is any sequence of non-space characters.
    + So non-alphanumeric things like apostrophes are part of words.
    + Examples: 
        + "Four" (4 letters)
        + "What's" (6 letters)
        + "seven." (6 letters)
- What about empty strings?
    + They will return an empty dictionary.
- What if there is more than one space between the words?
    + Directions say "consisting of zero or more space-separated words" so the
      number of spaces does not affect the output.

✱ RULES ✱
- solution must be in the form of a function
- spaces mark the end of words
- dictionary key must be the length of the word
    + punctuation is included as part of a word (counts towards the length)
    + the value must be the number of times it occurs in the string.
- the key & value order follows the word order in the input string, not in any
  ascending or descending order.

✱ EXAMPLES / TEST CASES ✱
- 'Four score and seven.' -> {4: 1, 5: 1, 3: 1, 6: 1}
- "What's up doc?" -> {6: 1, 2: 1, 4: 1}
- '' -> {}
- 'hello   clouds!' -> {4: 1, 7: 1}

✱ DS ✱
- A list of the words in the input string.
- An empty dictionary to collect the counts.

✱ ALGORITHM ✱
I: `txt`
[x] Initialize empty dictionary - `result`
[x] Initialize a list of the words in `txt`, using spaces as the separator 
   between words - assign to `words`.

[] For each word in `words`:
    [] Count the number of characters - assign to `length`
        [] If this number does not already exist in `result`,
            [] Add it to `result` - with `length` as the key, and 1 as the
               value.
        [] If this number already exists,
            [] increment the value with 1

[x] Return `result`
"""
def word_sizes(txt):
    result = {}
    words = txt.split()

    for word in words:
        length = len(word)
        if length not in result:
            result[length] = 1
        else:
            result[length] += 1

    return result

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1}) # True

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2}) # True

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1}) # True

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1}) # True

print(word_sizes('') == {}) # True

# LS SOLUTION
def word_sizes(words):
    words_list = words.split()
    counts = {}

    for word in words_list:
        word_size = len(word)
        if word_size not in counts:
            counts[word_size] = 0

        counts[word_size] += 1

    return counts

"""
The `word_sizes` function takes the input string and calls the `split()` string 
method on it, which splits it into a list of words separated by spaces and 
returns it. This is assigned to the variable `words_list`.

It creates an empty dictionary to hold the count of the letters.

It then iterates through `words_list` and for each word in it, it calls the 
`len()` function to count the number of characters in each string, and assigns
the returning integer to `word_size`. If that integer does not already exist in
the `counts` dictionary, it adds a new key-value pair, using `word_size` as the
key and `0` as its value. Then it increments the count by `1`.

So that means that if it already exists, adding a new key-value pair will be 
skipped, and the value for that count will be incremented by 1.

Then the `counts` dictionary is returned.

---
LS's solution does two things differently:
- Variable names: `counts` & `words_list` are more descriptive about the 
  purpose and type of data being stored.
- Single Responsibility Principle:
    + The conditional:
              if word_size not in counts:
            counts[word_size] = 0

        counts[word_size] += 1
      only handles initialization. Mine initializes AND increments, which are
      two distinct operations.

      This pattern of "initialize if needed, then always increment is common in
      counter implementations. It's useful when your counter logic might become
      more complex later.

      However, this is more about style & readability than correctness (as per
      LS Bot).
"""
