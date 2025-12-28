"""
Given a dictionary, return its keys sorted by the values associated with each 
key.
"""
"""
I: a dict
O: a list, sorted

Ex:
- {'p': 8, 'q': 2, 'r': 6} => ['q', 'r', 'p']

Rules:
- values dictate the order (numbers)
- sort in ascending order
- return only the keys as a list

DS/Brainstorm:
- sorted() -> returns a list
    - sorts by key
    - key= parameter
        - get
"""
def order_by_value(dictionary):
    return sorted(dictionary, key=dictionary.get)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
