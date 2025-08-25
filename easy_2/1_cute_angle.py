"""
Write a function that takes a floating point number representing an angle 
between 0 and 360 degrees and returns a string representing that angle in 
degrees, minutes, and seconds. You should use a degree symbol (`°`) to 
represent degrees, a single quote (`'`) to represent minutes, and a double 
quote (`"`) to represent seconds. There are 60 minutes in a degree, and 60 
seconds in a minute.

Note: You can use the following constant to represent the degree symbol:
"""
"""
I: the angle as an integer or a float
O: the angle as a string

Ex:
- 30 => "30°00'00\""
    - deg = 30
- 76.73 => "76°43'48\""
    - deg = 76
    - min = .73 * 60 = 43.8 = 43
    - sec = .8 * 60 = 48.0 = 48

Rules:
- degrees °
- minutes '
- seconds "
- 1 deg = 60 minutes
- 1 minute = 60 seconds
- if input is 0 or 360, return "0°00'00\""

Breakdown:
- degrees, minutes, seconds are the whole number part of each step
- get just the decimal part of a number (use % to divide by 1, get remainder)
- deg = int(angle_in_float)
- min = int((angle_in_float % 1) * 60))
- sec = int((min % 1) * 60)
- f-string to tie it all together

Algo:
- initialize `min` with the result of (angle_in_float % 1) * 60
- initialize `sec` with the result of (min % 1) * 60
- return f-string of joined integer versions of angle_in_float, min, sec
    - pad extra zeros with f"{v:02d}"

Step-Through:
I: 76.73
min = 43.80000000000024
sec = 48.000000000014325

I: 30
min = 0
sec = 0
need to pad them
"""
DEGREE = "\u00B0"

def dms(angle_in_float):
    min = (angle_in_float % 1) * 60
    sec = (min % 1) * 60
    return f"{int(angle_in_float)}{DEGREE}{int(min):02d}'{int(sec):02d}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
