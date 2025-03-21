"""
I: 6 numbers as inputs from user
O: strings that show what was entered as well as what nth number it is
O: string that show whether the last number is amongst the first 5

✱ EXAMPLES ✱
- Ex 1
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23. 

- Ex 2
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.

✱ QUESTIONS ✱
- What happens when the user inputs a non-integer value?
    - What happens when the user inputs a decimal number?
- Do the numbers have to be compared as strings or as numbers?
- Do the first 5 input numbers have to be outputted in order in the last line?

✱ RULES ✱
- Each input needs to be preceded by "Enter the [n]th/rd number: "
- Last input needs to be preceded by "Enter the last number: "
- Output must show whether the last input is in or not in the first 5 inputs.
    - Must be matched exactly
- Inputs must be numbers.
- Last input must be compared to the rest 

✱ TEST CASES ✱
- 

✱ DS ✱
- An empty list to collect the inputs.
- A list of words describing the place of the number ("1st", "3rd", "last") to
  be iterated over and outputted to console when getting input.
- A range object to iterate over 6 times.

✱ ALGORITHM ✱
[x] - Initialize empty list - `first_5`
[x] - Initialize list of ordinal words - `ordinal_words`
[x] - For each `word` in `ordinal_words`:
    [x] - If `word` is `"last"`:
        [x] + Get user input: "Enter the {`word`} number: " 
            [x] - Capture in `last_num` & Transform it into an integer.
    [x] - Else:
        [x] + Get user input: "Enter the {`word`} number: " 
            [x] - Capture input in `num` & Transform it into an integer.
            [x] + Append it to `first_5`
[x] - If `last_num` is in `first_5`:
    [x] + Print "`last_num` is in `first_5`"
        [NOTE: Extracted to `join_nums()`]
[x] - Else:
    [x] + Print "`last_num` isn't in `first_5`"

<-------- HELPER FUNCTION: `join_nums()` -------->
I: a list of nums - `num_list`
O: a string of the nums from the input list joined with a comma

✱ ALGO ✱
[x] - Join the numbers in `num_list` with a comma in between & return it.
<------------------------------>
"""
def search_for_last_num():
    first_5 = []
    ordinal_words = ['1st', '2nd', '3rd', '4th', '5th', 'last']

    for word in ordinal_words:
        if word == 'last':
            last_num = int(input(f'Enter the {word} number: '))
        else:
            num = int(input(f'Enter the {word} number: '))
            first_5.append(num)

    if last_num in first_5:
        print('')
        print(f'{last_num} is in {join_nums(first_5)}.')
    else:
        print('')
        print(f'{last_num} isn\'t in {join_nums(first_5)}.')


def join_nums(num_list):
    return ', '.join(str(num) for num in num_list)

search_for_last_num()
# Enter the 1st number: 5
# Enter the 2nd number: 6
# Enter the 3rd number: 4
# Enter the 4th number: 2
# Enter the 5th number: 3
# Enter the last number: 5

# 5 is in 5, 6, 4, 2, 3.

search_for_last_num()
# Enter the 1st number: 8
# Enter the 2nd number: 9
# Enter the 3rd number: 5
# Enter the 4th number: 2
# Enter the 5th number: 66
# Enter the last number: 4

# 4 isn't in 8, 9, 5, 2, 66.

# FUTHER EXPLORATION
# Suppose we alter the problem to look for a number that satisfies a condition 
# (e.g., a number greater than 25) instead of a specific number? Would the 
# current solution still work? Why or why not?

# The current solution will not work because the `in` is used for membership
# testing only, meaning it can only tell us if a specific value exists in a
# collection, not if any element meets a certain condition.
