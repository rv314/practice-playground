'''
Given a time in

-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
s = '12:01:00PM'
Return '12:01:00'.

s = '12:01:00AM'
Return '00:01:00'.

'''

#!/bin/python3

import os
import re


def timeConversion(s):
    # Grab AM or PM string
    ap = s.split(":")[2][2:]
    # Create list of hh:mm:ss stripping AM or PM
    time_list = re.sub(r"[A-Z]+", "", s).split(":")
    
    final = None
    
    if ap == "PM" and int(time_list[0]) != 12:
        time_list[0] = str(int(time_list[0]) + 12)
        final = ":".join(time_list)
    elif ap == "AM" and int(time_list[0]) == 12:
        time_list[0] = str(int(time_list[0]) - 12) + "0"
        final = ":".join(time_list)
    else:
        final = ":".join(time_list)
        
    return final
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
