"""
Create a function that takes two integers as arguments. The first argument is a
count, and the second is the starting number of a sequence that your function 
will create. The function should return a list containing the same number of 
elements as the `count` argument. 

The value of each element should be a multiple of the starting number.

You may assume that `count` will always be an integer greater than or equal to 
`0`. The starting number can be any integer. If the `count` is `0`, the 
function should return an empty list.
"""
"""
I: integer, count
I: integer, the starting number
O: a list of numbers

Rules:
- the `count` is the length of the output list
    - if `count` is 0, return an empty list
- starting number is the multiple of all elements in output list
- must be looped until length is the same as the given count

DS/Brainstorm:
- guard clause for count == 0
- for loop since we know how many iterations we need
- range object (to generate numbers to multiply starting_num with)
    - start at 1
    - stop at `count` + 1

Algo:
- if `count` is 0, return empty list
- iterate through a list of numbers from 1 to count + 1
    - multiply each number with starting number
    - populate new list with the results
- return resulting list
"""
def sequence(count, starting_num):
    return [num * starting_num for num in range(1, count + 1)]

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True

"""
Option 2:
- while loop
    - loop until the length of result list is the same as `count`

Algo:
- initialize `multiplier` with 1
- initialize `result` with an empty list
- while the length of result is less than `count`:
    - multiply `start` with `multiplier`
    - add the result to `result` list
    - increment multiplier by 1
- return result
"""
def sequence(count, start):
    multiplier = 1
    result = []

    while len(result) < count:
        result.append(start * multiplier)
        multiplier += 1

    return result
