"""
Write a function that takes a list of numbers and returns a list with the same 
number of elements, but with each element's value being the running total from 
the original list.
"""
"""
I: a list of numbers or an empty list
O: another list of numbers, each the running total

Ex:
- [2, 5, 13] => [2, 7, 20]
    - 2
    - 2 + 5 = 7
    - 7 + 13 = 20

Breakdown:
- a list to gather values
- a variable to keep track of current total
- iterate through numbers:
    - add total to each number
    - append the result to the result list

Algo:
- SET `result` = []
- SET `total` = 0
- for num in numbers:
    - add num to total
    - append result to `result`
- return `result`
"""
def running_total(numbers):
    result = []
    total = 0

    for num in numbers:
        total += num
        result.append(total)

    return result

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
