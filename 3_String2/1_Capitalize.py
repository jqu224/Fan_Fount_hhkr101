#!/bin/python3
Sample Input
  chris alan
  
Sample Output
  Chris Alan

-----------------------------------------


import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # # doesnt work
    # temp = s.split()
    # for i in range(len(temp)):
    #     if temp[i].title()[0] != temp[i][0]:
    #         temp[i] = temp[i].title()

    # solution a
    temp = list(s)
    counter = 0
    for i, char in enumerate(temp):
        if char == " ":
            counter = 0
        elif counter == 0:
            temp[i] = temp[i].upper()
            counter += 1
        else:
            counter += 1
    return("".join(temp))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
