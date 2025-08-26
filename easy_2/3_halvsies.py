"""
Write a function that takes a list as an argument and returns a list that 
contains two elements, both of which are lists. Put the first half of the 
original list elements in the first element of the return value and put the 
second half in the second element. If the original list contains an odd number 
of elements, place the middle element in the first half list.
"""
"""
I: a list
O: a list of nested lists

Rules:
- if the length of the list is even:
    - put the first half in the first nested list
    - put the second half in the 2nd nested list
- if the length of the list is odd:
    - do the same as even but place the middle one in the first half

Breakdown:
- get the length of the input list
- initialize `result` with an empty list
- initialize `mid` with len(lst) // 2
    + ex: [1, 2, 3, 4]
        + mid = 2
        + indices 0-2 (2 exclusive) slice
        + indices 2-end slice
- if the length is even:
    - append the first half slice of the list to result (lst[:mid])
    - append the second half slice of the list to result (lst[mid:])
- else:
    - append first half slice to result (lst[:mid+1])
    - append second half slice to result (lst[mid-1:])
- return result
"""
def halvsies(lst):
    mid = len(lst) // 2
    result = []
    
    if len(lst) % 2 == 0:
        result.append(lst[:mid])
        result.append(lst[mid:])
    else:
        result.append(lst[:mid+1])
        result.append(lst[mid+1:])

    return result

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]]) # True
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]]) # True
print(halvsies([5]) == [[5], []]) # True
print(halvsies([]) == [[], []]) # True

# LS Solution
def halvsies(lst):
    half = (len(lst) + 1) // 2
    first_half = lst[:half]
    second_half = lst[half:]
    return [first_half, second_half]

"""
`half = (len(lst) + 1) // 2` works because if you add 1 to an even number
before dividing by 2 with floor division still returns the same answer since
floor division truncates the decimal part.
"""
