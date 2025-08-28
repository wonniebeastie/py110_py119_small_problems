"""
Write a function that takes one argument, a list of integers, and returns the 
average of all the integers in the list, rounded down to the integer component 
of the average. The list will never be empty, and the numbers will always be 
positive integers.
"""
"""
I: a list of numbers
O: average of all numbers in the list, as int

Rules:
- list will never be empty
- numbers will always be positive
- output is rounded down

Breakdown:
- initialize `total` to 0
- iterate through list, and for each number:
    - add it to total
- floor divide total by the length of the input list & return it
"""
def average(numbers):
    total = 0
    for num in numbers:
        total += num

    return total // len(numbers)

# Refactored
def average(numbers):
    return sum(numbers) // len(numbers)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True
