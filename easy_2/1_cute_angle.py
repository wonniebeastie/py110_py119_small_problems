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


"""
SECOND APPROACH:
If the f-string format specification can't be used for whatever reason:

Algo:
- initialize `min` with the result of (angle_in_float % 1) * 60
- initialize `sec` with the result of (min % 1) * 60
- return f-string of joined integer version of angle_in_float, the result of
  pad_zeros(min), and the result of pad_zeros(sec)

-- HELPER (`pad_zeros()`) --
I: an integer, min or sec
O: the input padded with another zero, as strings

Algo:
- turn input into an integer,
- turn integer into a string
- if length of the string is 1:
    - concatenate "0" to the beginning of the string & return it
- return it

0 -> 0 -> "0" ->
2.23493 -> 2 -> "2" ->
35.654543 -> 35 -? "35" ->
"""
DEGREE = "\u00B0"

def dms(angle_in_float):
    min = (angle_in_float % 1) * 60
    sec = (min % 1) * 60
    return f"{int(angle_in_float)}{DEGREE}{pad_zeros(min)}'{pad_zeros(sec)}\""

def pad_zeros(num):
    num = str(int(num))
    if len(num) == 1:
        return "0" + num
    return num

"""
DEBUGGING NOTES:

Problem:
- sec is not being calculated correctly due to the `int()` in min

Options: [DID NOT WORK]
- remove int from min 
    - min will not be truncated
        - Problem: meaning that the pad_zeros() will receive possibly 
          a long int, and change it into a string
            - Option: move the int() to inside pad_zeros()
                - 2.0863800000000765 -> 2 -> "2"
                - "0" + "2"
                - "02"

Problem: the zeros are covered because their length is 1, but
the long floats are not being covered by the if conditions

Problem: the test cases with non-zero numbers for both places are
not being truncated properly.

Option 1: [DID NOT WORK]
- put int() for both min and sec in the return line 
    - does not work because turning the strings into integers makes
      them short again "00" -> 0

Option 2: [WORKED!]
- change pad_zeros function
    - if input is 0: get padded with "0" in front
    - if input is a single non-zero number (i.e. 2 or 5), then:
        - truncated it to lose the decimal part
        - also pad with "0" in front
    - if input has non-zeros for both places, then just return the
      integer version
"""
