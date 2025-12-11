"""
Write a function that takes a string argument consisting of a first name, a 
space, and a last name. The function should return a new string consisting of 
the last name, a comma, a space, and the first name.

You may assume that the names don't include middle names, initials, or suffixes
("Jr.", "Sr.").
"""
# Using unpacking
def swap_name(name):
    first, last = name.split()
    return f"{last}, {first}"

# Using slicing to reverse before joining
def swap_name(name):
    return ", ".join(name.split()[::-1])

# Using indexing after splitting
def swap_name(name):
    name_list = name.split()
    return f"{name_list[1]}, {name_list[0]}"

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

# FURTHER EXPLORATION
def swap_name(name):
    name = name.split()
    return f"{name[-1]}, {' '.join(name[0:-1])}"

print(swap_name('Karl Oskar Henriksson Ragvals') 
                == "Ragvals, Karl Oskar Henriksson")  # True
