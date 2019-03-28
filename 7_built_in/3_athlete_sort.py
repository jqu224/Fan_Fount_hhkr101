#!/bin/python3

import math
import os
import random
import re
import sys

# first define a 
def takeSecond(elem):
    return elem[k]
 
 

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []
  
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        
    k = int(input())

    #    #     #     #     #     #     #     # 
    # solution a
    sted = sorted(arr, key=takeSecond)
    for i in range(len(sted)):
        print(" ".join(map(str, sted[i])))

    #    #   #     #     #     #     #     # 
    # solution a.2
    # same thing as 
    sted = sorted(arr, key=lambda x: x[k])
    for i in range(len(sted)):
        print(" ".join(map(str, sted[i])))


    # #     #     #     #     #     #     #     # 
    # # solution b
    sted = sorted(arr, key=takeSecond) 
    print("\n".join([" ".join(map(str, sted[i])) for i in range(len(sted))]))
    
