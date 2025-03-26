"""
I: a list of numbers
O: a list of the running total from the og list

✱ QUESTIONS ✱
- What is "running total" mean?
    + Running total means the sum of all previous numbers including the current
      number.
- Does the returning list have to be a new object or should the og list be
  modified? 
- What happens if the input list is empty?
    + The output list will also be empty. 
- What happens if there is only a single value in the list?
    + The output list will be the same as the input list.
- What if the input list has negative numbers?
- What if there are multiple zeros in the input list?

✱ RULES ✱
- returning list must be same number of elements
- each element's value must be the sum of the previous numbers that came before
  it, including itself.

✱ EXAMPLES / TEST CASES ✱
- [2, 5, 13] -> [2, 7, 20]
- [14, 11, 7, 15, 20] -> [14, 25, 32, 47, 67]
- [3] → [3]
- [] → []
Edge Cases:
- [-1, -2, -3] -> [-1, -3, -6]
- [5, -3, 1] -> [5, 2, 3]
- [0, 0, 0] -> [0, 0, 0]
- [0, 1, 0] -> [0, 1, 1]

✱ DS ✱
- An empty list to store the running totals.
- A variable to track the running total so far.

✱ ALGORITHM ✱
I: `num_list`
[] Initialize variable `result` with an empty list.
[] Initialize variable `current_total` with 0.
[] For each number in `num_list`: 
    [] Add number to `current_total` 
    [] Append `current_total` to `result` list.
[] Return `result`

"""
def running_total(num_list):
    result = []
    current_total = 0

    for num in num_list:
        current_total += num
        result.append(current_total)

    return result

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

