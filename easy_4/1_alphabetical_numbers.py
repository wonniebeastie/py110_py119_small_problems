"""
Write a function that takes a list of integers between 0 and 19 and returns a 
list of those integers sorted based on the English word for each number:

zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, 
twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
"""
"""
I: a list, of integers
O: a list, of integers (sorted alphabetically)

Ex:
- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
   10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
=> [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
    7, 17, 6, 16, 10, 13, 3, 12, 2, 0]
    - eight, eighteen, eleven...zero

Rules:
- integers must be mapped with their english counterparts

DS/Brainstorm:
- assume output is a new list
- [zero, one, two, three...] 0, 1, 2, 3
    - already in ascending order
- {0: zero, 1: one, 2: two, }
- sorted() => new list
    - key= helper function that maps their english words
    - already sorts strings in alphabetical order

Helper -> map ints with their english counterparts (map_int)
    I: int, the number/index
    O: str, english word of that integer
    - SET eng_nums to list:
      ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    - return eng_nums[int]
    2 => two
"""
def alphabetic_number_sort(numbers):
    return sorted(numbers, key=map_int)

def map_int(num):
    eng_nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    return eng_nums[num]

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True

# list.sort() can be used as well, but since the problem doesn't specify if it
# wants the output list to be the original or a new list, using sorted() saves
# us a line.
