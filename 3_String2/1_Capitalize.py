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
            counter = 1 
    return("".join(temp))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

    
    
+++++++++++++++++++++     NOTE      NOTE       NOTE     ++++++++++++++++++++++
    
    
counter 用来记录当前是不是 单个word 的第一个字母，如果是，把这个字母upper case，然后counter +1
碰到空格，counter变回 0 
譬如 “ac wf”
for i,a in enumerate(list_temp): i是index数字，a是一个个char
    i == 0 counter == 0 则 list[0] = list[0].upper() -> "a" 变成"A" 然后 counter +1
    i == 1 counter == 1 此时 char == "c" 说明这时候不是首字母，不要管他，else可写可不写。
    i == 2 counter == 2 此时 char == " " 进入 if char == " " 更新 counter = 0
    i == 3 counter == 0 此时 char == "w" 进入 elif counter == 0 更新  list[3] = list[3].upper() -> "w" 变成"W" 
