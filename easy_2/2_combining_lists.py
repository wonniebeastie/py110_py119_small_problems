"""
Write a function that takes two lists as arguments and returns a set that 
contains the union of the values from the two lists. You may assume that both 
arguments will always be lists.
"""
# Approach using the union set operator
def union(lst1, lst2):
    return set(lst1) | set(lst2)

# Approach using the union method
def union(lst1, lst2):
    return set(lst1).union(lst2)

# Approach using list concatenation
def union(lst1, lst2):
    return set(lst1 + lst2)

# Manual approach
"""

"""

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
