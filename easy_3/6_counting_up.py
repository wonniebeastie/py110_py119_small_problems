"""
Write a function that takes an integer argument and returns a list containing 
all integers between `1` and the argument (inclusive), in ascending order.

You may assume that the argument will always be a positive integer.
"""
"""
I: an integer
O: a list containing all numbers between 1 & input integer (ascending)

Breakdown:
Option 1:
- use a range object starting from 1, ending at length of sequence + 1
    - add each number into a list
Option 2:
- start at 1 (`count`)
- use a while loop to add each count to a list as long as the count is less
  than the input number
"""
# Option 1
def sequence(num):
    result = []
    for count in range(1, num + 1):
        result.append(count)

    return result

# Refactored
def sequence(num):
    return [n for n in range(1, num + 1)]

# Or
def sequence(num):
    return list(range(1, num + 1))

# Option 2
def sequence(num):
    count = 1
    result = []

    while count < num + 1:
        result.append(count)
        count += 1

    return result

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True
