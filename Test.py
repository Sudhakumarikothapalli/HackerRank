#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    res = ''
    l = s.split(":")
    if "AM" in l[2]:
        if l[0] == '12':
            l[0] = '00'
            l[2] = l[2][:-2]
            res = ":".join(l)
        else:
            l[2] = l[2][:-2]
            res = ":".join(l)
    elif "PM" in l[2]:
        if l[0] != '12':
            l[0] = str(int(l[0]) + 12)
            l[2] = l[2][:-2]
            res = ":".join(l)
        else:
            l[2] = l[2][:-2]
            res = l.join(":")   
    else:
        print("Invalid Input")
    print(res)

if __name__ == '__main__':
    s = input()
    timeConversion(s)