"""
The time of day can be represented as the number of minutes before or after 
midnight. If the number of minutes is positive, the time is after midnight. If 
the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns 
the time of day in 24-hour format (hh:mm). Your function should work with any 
integer input.

You may not use Python's `datetime` module.

Disregard Daylight Savings and Standard Time and other complications.
"""
"""
I: a positive or negative integer (number of minutes)
O: a string representing # of minutes before or after midnight (24hr format)

Rules:
- 0 is midnight
- positive number == AFTER midnight
- negative number == BEFORE midnight

Ex:
- 800 => "13:20"
    - 800 minutes after midnight
    - 800 % 1440 = 800
    - 800 // 60 = 13 hrs
    - 800 % 60 = 20 minutes
- 3000 => "02:00"
    - 3000 minutes after midnight
    - 3000 % 1440 = 120
    - 120 // 60 = 2 hrs
    - 120 % 60 = 0 minutes
- -3 => "23:57"
    - 3 minutes before midnight
    - -3 % 1440 = 1437
    - 1437 // 60 = 23 hrs
    - 1437 % 60 = 57 minutes
- -4231 => "01:29"
    - 4231 minutes before midnight
    - -4231 % 1440 = 89
    - 89 // 60 = 1 hr
    - 89 % 60 = 29 min

Breakdown:
- 1440 minutes in 24 hours (60m in 1 hr, so 60 * 24 = 1440)
- negative input = clock goes backwards
- if input is over 1440 minutes, then that means the clock "wraps around" a 
  full circle x number of times (input / 1440 = x)
    - this means that x can be disregarded since the clock resets every 24 hrs
    - the modulo operator gives you the remainder while also accounting for the
      "wrap around"s
    - so regardless of whether the input is positive or negative, under or over
      1440, it doesn't matter, we just need the remainder of the input divided
      by 1440
"""
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = 1440

def time_of_day(minutes):
    mins_within_24h = minutes % MINUTES_PER_DAY
    hr = mins_within_24h // MINUTES_PER_HOUR
    mins = mins_within_24h % MINUTES_PER_HOUR

    return f"{hr:02d}:{mins:02d}"

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
