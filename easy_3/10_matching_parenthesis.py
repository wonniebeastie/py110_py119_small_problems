"""
Write a function that takes a string as an argument and returns `True` if all 
parentheses in the string are properly balanced, `False` otherwise. To be 
properly balanced, parentheses must occur in matching `'(' and ')'` pairs.
"""
"""
I: a str
O: a boolean

Ex:
- "What is) this?" == False
- "Hey!" == True
    - doesn't have any so it's "balanced"
- ")Hey!(" == False
    - both appear
- "((What) (is this))?" == True
- "((What)) (is this))?" == False
    - remaining right one

Rules:
- return true if all parentheses in input string are "properly balanced"
    - false otherwise
- "properly balanced" means each '(' has a matching ')' (pairs)
- for every single '(' left one, there has to be a ')' right one,
    - doesn't have to be in order
- if it starts out with the right side ')', then not balanced

DS/Brainstorm:
1) if we encounter a ')' right pair FIRST = not balanced
2) if we iterate through the entire string w/o encountering any pair =
   balanced
3) if we encounter a '(' left pair, right pair ')' is found = balanced
4) if we encounter a '(' left pair, but no right pair ')' = not balanced

- for each char:
    - 1 for each left pair
    - -1 for each right pair
    - check balance
        - if balance < 0: return false
        - if balance > 0: keep going

- at the end:
    - if balance == 0 then it means it's balanced -> return True
    - if balance != 0 then it's unbalanced -> return False


Algo:
    - SET balance to 0
    
    - for char in txt:
        - if char is '(':
            - increment balance by 1
        - else if char is ')':
            - decrement balance by 1
        - check if balance is less than 0:
            - if it is: return false

    - return true if balance is 0, return false otherwise

Walkthrough:
    ")Hey!("
    balance = -1
    check balance - less than 0, return false

    "((What) (is this))?" => true
    balance = 0 return true
"""
def is_balanced(txt):
    balance = 0

    for char in txt:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False

    return balance == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
