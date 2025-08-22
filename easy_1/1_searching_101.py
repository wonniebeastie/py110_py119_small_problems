"""
Write a program that solicits six (6) numbers from the user and prints a 
message that describes whether the sixth number appears among the first five.

Example 1:
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.

Example 2:
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.
"""
numbers = []

numbers.append(input("Enter the 1st number: "))
numbers.append(input("Enter the 2nd number: "))
numbers.append(input("Enter the 3rd number: "))
numbers.append(input("Enter the 4th number: "))
numbers.append(input("Enter the 5th number: "))
last = input("Enter the last number: ")

if last in numbers:
    print(f"{last} is in {', '.join(numbers)}.")
else:
    print(f"{last} isn't in {', '.join(numbers)}.")

# FURTHER EXPLORATION
"""
The above solution will not work if you're looking for a number that meets a 
certain condition like being greater than `25` because `in` checks whether a 
specific value exists or not in an iterable. 
"""
numbers = []
suffixes = ["1st", "2nd", "3rd", "4th", "5th"]

for suffix in suffixes:
    numbers.append(int(input(f"Enter the {suffix} number: ")))

if any(num > 25 for num in numbers):
    print(f"Yes, a number greater than 25 exists in {', '.join([str(num) for num in numbers])}.")
else:
    print(f"No, a number greater than 25 does not exist in {', '.join([str(num) for num in numbers])}.")
