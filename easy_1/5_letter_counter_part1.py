"""
Write a function that takes a string consisting of zero or more space-separated 
words and returns a dictionary that shows the number of words of different 
sizes.

Words consist of any sequence of non-space characters.
"""
"""
I: a sentence or an empty string
O: a dictionary (keys = lengths)

Ex:
- 'Four score and seven.' => {4: 1, 5: 1, 3: 1, 6: 1}
    - Four = 4 
    - score = 5
    - and = 3
    - seven = 6

- "What's up doc?" => {6: 1, 2: 1, 4: 1}
    - What's = 6
    - up = 2
    - doc? = 4

Rules:
- word = any sequence of non-space characters
- special characters like punctuation counts

Breakdown:
- split txt into a list of words
- iterate through the list of words, and for each word:
    - get the length of the word => becomes the key
    - get the number of times that word occurs in the list => becomes the value
- return the dictionary
"""
def word_sizes(txt):
    counts = {}

    for word in txt.split():
        counts[len(word)] = counts.get(len(word), 0) + 1

    return counts

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



# Without using the `.get()` method
"""
- counts = empty dictionary
- iterate through each word in split list of words:
    - SET `length` = length of each word
    - if length doesn't exist in `counts` dictionary:
        - add the length as the key, along with the value 0
    - increment the value by 1
- return counts
"""
def word_sizes(txt):
    counts = {}
    
    for word in txt.split():
        length = len(word)
        if length not in counts:
            counts[length] = 0
        counts[length] += 1

    return counts
