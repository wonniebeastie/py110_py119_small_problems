"""
As seen in the previous exercise, the time of day can be represented as the 
number of minutes before or after midnight. If the number of minutes is 
positive, the time is after midnight. If the number of minutes is negative, the
time is before midnight.

Write two functions that each take a time of day in 24 hour format, and return 
the number of minutes before and after midnight, respectively. Both functions 
should return a value in the range 0 through 1439.

You may not use Python's datetime module.
"""
"""
As seen in the previous exercise, the time of day can be represented as the 
number of minutes before or after midnight. If the number of minutes is 
positive, the time is after midnight. If the number of minutes is negative, the
time is before midnight.

Write two functions that each take a time of day in 24 hour format, and return 
the number of minutes before and after midnight, respectively. Both functions 
should return a value in the range 0 through 1439.

You may not use Python's datetime module.
"""
"""
-- AFTER MIDNIGHT -->
I: a string, the time in 24 hr format
O: an integer, the number of minutes after midnight

Ex:
- "12:34" => 754 minutes
    - 12 * 60 = 720
    - 720 + 34 = 754
    - 754 % 1440 = 754

Rules:
- "00:00" and "24:00" are both midnight, so should return 0

Algo:
- split input into two parts - before the ":" and after it
- convert first part into integer 
- convert second part into integer (`remaining_min`)
- multiply hrs by 60 get number of hours in minutes (`hrs_in_min`)
- add remaining_min to the result
- get remainder after dividing the result from above by 1440


-- BEFORE MIDNIGHT -->
I: a string, the time in 24 hr format
O: an integer, the number of minutes before midnight

Ex:
- "12:34" => 686 minutes
    - 12 * 60 = 720
    - 720 + 34 = 754
    - 754 % 1440 = 754
    ---
    - 1440 - 754 = 686
- "24:00" => 0
    - 24 * 60 = 1440
    - 1440 + 0 = 1440
    - 1440 % 1440 = 0
    ---
    - 1440 - 0 = 1440

Algo:
- get result from `after_midnight(input)`
- subtract this result from 1440 (`delta_minutes`)
- if delta_minutes == 1440:
    - reassign delta_minutes with 0
- return delta_minutes
"""
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def after_midnight(time_str):
    hrs, remaining_min = [int(unit) for unit in time_str.split(":")]
    return ((hrs * MINUTES_PER_HOUR) + remaining_min) % MINUTES_PER_DAY

def before_midnight(time_str):
    delta_minutes = MINUTES_PER_DAY - after_midnight(time_str)
    if delta_minutes == MINUTES_PER_DAY:
        delta_minutes = 0
    return delta_minutes

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
