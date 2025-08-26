"""
Write a function that combines two lists passed as arguments and returns a new 
list that contains all elements from both list arguments, with each element 
taken in alternation.

You may assume that both input lists are non-empty, and that they have the same
number of elements.
"""
# Option 1 with `zip()` & extend
def interleave(lst1, lst2):
    zipped_lists = zip(lst1, lst2)

    result = []
    for pair in zipped_lists:
        result.extend(pair)

    return result

"""
`extend` works in a single `for` loop because it adds elements from each pair
individually. Using `append` like this would create a nested list because it
would add the entire pair as a single element.
"""

# Option 2 with `zip()` & append
def interleave(lst1, lst2):
    zipped_lists = zip(lst1, lst2)

    result = []
    for pair in zipped_lists:
        for value in pair:
            result.append(value)

    return result

# Option 3 with `zip()` & a nested comprehension
def interleave(lst1, lst2):
    zipped_lists = zip(lst1, lst2)

    return [value for pair in zipped_lists
                  for value in pair]

# Option 4 with a range & `extend`
def interleave(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        result.extend([lst1[i], lst2[i]])

    return result

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
