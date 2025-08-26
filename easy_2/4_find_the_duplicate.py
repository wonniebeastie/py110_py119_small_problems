"""
Given an unordered list and the information that exactly one value in the list 
occurs twice (every other value occurs exactly once), determine which value 
occurs twice. Write a function that finds and returns the duplicate value.

You may assume that the input list will always have exactly one duplicate 
value.
"""
"""
I: a list of numbers
O: the integer value that occurs twice

Rules:
- input will only have exactly one duplicate value

Breakdown:
- Option 1:
    - iterate through numbers and get a count of how many times that
      value occurs in the list
        - `.count()` list method
        - if count method returns a value greater than 1, return that
          value
- Option 2:
    - iterate through the list and for each number, check if that value
      exists in the rest of `numbers`
        - if `in` returns `True`, then return that value
- Option 3:
    - create a frequency map of the counts of each value in the list
    - return the key associated with the value that is greater than 1
"""
# Option 1
def find_dup(numbers):
    for num in numbers:
        count = numbers.count(num)

        if count > 1:
            return num
"""
Repeatedly calling `.count()` on each item in the list can be inefficient since
`count` goes through the entire list each time (slower for longer lists).
"""

# Option 2
def find_dup(numbers):
    for i in range(len(numbers)):
        if numbers[i] in numbers[i+1:]:
            return numbers[i]

# Option 2 using `enumerate()`
def find_dup(numbers):
    for idx, num in enumerate(numbers):
        if num in numbers[idx+1:]:
            return num
"""
Option 2 avoids going through every single item in the list but it can still be
costly for large inputs due to slicing and membership checks.
"""

# Option 3
def find_dup(numbers):
    # Create a frequency map of counts
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    for num, count in counts.items():
        if count > 1:
            return num
"""
Option 3 builds the frequency map in one pass, then iterate through it to find
the duplicate, which can be more efficient than repeated counting but it uses
extra memory.
"""

# Option 4
def find_dup(numbers):
    counts = [num for num in numbers if numbers.count(num) == 2]
    return counts[0]
"""
This creates a list of the numbers that occur more than once in the input list.
Then you return the number at the first index since you only need one of them.

Option 4 has the same issue as Option 1 with calling `count` on every item.
"""

# Option 5
def find_dup(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return num

        seen.add(num)
"""
This uses an empty set and while iterating through `numbers`, if the number is
already in the `seen` set, it returns that number or if it's already in it, the
number just gets added to the set.

Option 5 is the most efficient out of all the options because membership checks
on sets are fast and stops immediately once a duplicate is found.
"""

print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True
