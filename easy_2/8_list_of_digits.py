"""
Write a function that takes one argument, a positive integer, and returns a 
list of the digits in the number.
"""
"""
I: an integer
O: a list containing the same digits as input integer

Algo:
- initialize empty list to accumulate elements
- convert integer to string
- iterate through string
    - for each digit:
        - convert them back into integers
        - add them to the new list
- return list
"""
def digit_list(num):
    return [int(num) for num in str(num)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

"""
I don't need to convert the string version of the number to a list because
strings are already iterable.
"""
