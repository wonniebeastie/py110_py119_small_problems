"""
Write a function that counts the number of occurrences of each element in a 
given list. Once counted, print each element alongside the number of 
occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").
"""
"""
I: a list of cars
O: a string in the format "{car} => {num}" 

Rules:
- case sensitive
- get a count of the number of times the element occurs in the input list

Breakdown:
- create a frequency map of elements
- iterate through dictionary of counts:
    - for each key value pair:
        - use an f-string to embed each key and value to match output
"""
def count_occurrences(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    
    for item, count in counts.items():
        print(f"{item} => {count}")

# Using a dictionary comprehension
def count_occurrences(lst):
    counts = {item: lst.count(item) for item in lst}
    
    for item, count in counts.items():
        print(f"{item} => {count}")

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
"""
Expected output:
# your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 1
motorcycle => 2
"""
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2

# My test case
vehicles2 = ['car', 'Car', 'truck', 'car', 'SUV', 'Truck',
            'motorcycle', 'motorcycle', 'Car', 'truck']

count_occurrences(vehicles2)
# car => 2
# Car => 2
# truck => 2
# SUV => 1
# Truck => 1
# motorcycle => 2



# FURTHER EXPLORATION
# Solve the problem when words are case insensitive - "suv" == "SUV"

def count_occurrences(lst):
    counts = {item: lst.count(item) for item in lst}
    
    for item, count in counts.items():
        print(f"{item} => {count}")

vehicles = ['car', 'Car', 'truck', 'car', 'SUV', 'Truck',
            'motorcycle', 'motorcycle', 'Car', 'truck']

count_occurrences(vehicles2)
# car => 4
# truck => 3
# suv => 1
# motorcycle => 2
