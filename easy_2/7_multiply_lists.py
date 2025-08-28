"""
Write a function that takes two list arguments, each containing a list of 
numbers, and returns a new list that contains the product of each pair of 
numbers from the arguments that have the same index. 

You may assume that the arguments contain the same number of elements.
"""
"""
I: 2 lists of numbers
O: a new list containing product of each pair of numbers

Breakdown:
- pair off each number with their corresponding one in the other list
    - zip to zip each pair together
- iterate through zipped iterable, for each pair:
    - multiply them together
    - add to new list
"""
# APPROACH 1 with `zip()`
def multiply_list(lst1, lst2):
    result = []
    pairs = zip(lst1, lst2)

    for num1, num2 in pairs:
        result.append(num1 * num2)

    return result

# Aprroach 1 refactored
def multiply_list(lst1, lst2):
    return [n1 * n2 for n1, n2 in zip(lst1, lst2)]

# APPROACH 2 with a range object
def multiply_list(lst1, lst2):
    result = []
    
    for i in range(len(lst1)):
        result.append(lst1[i] * lst2[i])
    
    return result

# Approach 2 refactored
def multiply_list(lst1, lst2):
    return [lst1[i] * lst2[i] for i in range(len(lst1))]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
