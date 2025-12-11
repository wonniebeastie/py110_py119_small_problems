"""
Write a function that takes a list as an argument and reverses its elements, in
place. That is, mutate the list passed into the function. The returned object 
should be the same object used as the argument.

You may not use the `list.reverse` method nor may you use a slice (`[::-1]`).
"""
"""
I: a list
O: the same list, mutated to be reversed

Ex:
- [1, 2, 3, 4] => [4, 3, 2, 1]
- ["abc"] => ["abc"]
- [] => []

Rules:
- Can't use the list.reverse method nor slicing [::-1]

DS/Brainstorm:
- Idea 1: Create a copy of the original list, remove everything from the 
original list, and then add the values from the copy, but backwards.
    - range(start, stop, step) 0,1,2,3
        - start at last one (len(lst) - 1) 3, 2, 1, 0
        - stop at first one (-1)
            - stop values are exclusive so a 0 stops at 1
            - to get actual 0, we want to use -1
        - step value of -1

Algo for Idea 1:
    - SET copied_list to a copy of the original list
    - clear out the elements from the original list (.clear method)
    - Iterate through each index of copied_list backwards:
        - append the element at each index to original list
    - return the original list
"""
# IDEA 1 - utilizing a copy
def reverse_list(lst):
    copied_list = lst[:]
    lst.clear()
    for i in range(len(copied_list) - 1, -1, -1):
        lst.append(copied_list[i])
    return lst

# Another copy idea - makes use of list.insert() method
"""
Algo:
    - SET copied_list to a copy of original list
    - clear the original list
    - for each num in copied_list:
        - insert num at index 0 of original list
    - return original list
"""
def reverse_list(lst):
    copied_list = lst.copy() # copy [1, 2, 3, 4]
    lst.clear() # []

    for num in copied_list: # 1, 2, 3, 4
        lst.insert(0, num) # [1], [2, 1], [3, 2, 1], [4, 3, 2, 1]

    return lst

# IDEA 2
"""
...

- Idea 2: 
    Iterate through the original list, and swap the current element
    with the last element, increment the backwards index til it meets in the 
    middle.
        - need to iterate forwards
        - but also backwards
        - stop at the middle
 
...

Algo for Idea 2:
    - SET backwrds_idx to -1
    - SET mid to the result of floor dividing the length of lst by 2
    - for each index of lst, until middle index:
        - SET lst[backwrds_idx], lst[current idx] = lst[current index], lst[backwrds_idx]
        - decrement backwrds_idx by 1
    - return lst

Walkthrough:
    [1, 2, 3, 4]  0, 1, 2, 3 (stop at index 2), -1, -2
    [4, 2, 3, 1] - 1 & 4
    [4, 3, 2, 1] - 2 & 3
"""
def reverse_list(lst):
    backwrds_idx = -1
    mid = len(lst) // 2
    for i in range(mid):
        lst[backwrds_idx], lst[i] = lst[i], lst[backwrds_idx]
        backwrds_idx -= 1
    return lst

# IDEA 2 Refactored/LS's Solution
def reverse_list(lst):
    first = 0
    last = -1

    while first < (len(lst) // 2):
        lst[first], lst[last] = lst[last], lst[first]
        first += 1
        last -= 1

    return lst

# Using a while loop makes more sense than a for loop like I did.

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True
