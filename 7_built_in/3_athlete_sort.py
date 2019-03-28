https://www.hackerrank.com/challenges/python-sort-sort/problem
    
    #!/bin/python3

import math
import os
import random
import re
import sys

# first define an anonymous function
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
    # same thing as solution (a) but not using line 10-11   
    # 这里 lambda 和 takesecond 一样，都是建立了一个 anonymous 未名 function
    # 返回的是：一个还没输入的 list 的第k个值  或者  一个还没输入的 tuple 的第 k 个值 
    # 用在这里，代表着：按照arr的第二个值，来sort。
    sted = sorted(arr, key=lambda x: x[k])
    for i in range(len(sted)):
        print(" ".join(map(str, sted[i])))


    # #     #     #     #     #     #     #     # 
    # # solution b
    sted = sorted(arr, key=takeSecond) 
    print("\n".join([" ".join(map(str, sted[i])) for i in range(len(sted))]))
    
    
````````````````````````````````````````````````````````````
# 你把 key 当作 condition function 理解，按 key 的条件来
strs = ['ccc', 'aaaa', 'd', 'bb']
print sorted(strs, key=len)  ## ['d', 'bb', 'ccc', 'aaaa']
这里key = len意思是按照 key = len()这个条件来sort
看似和a2写法完全不同，但是。。。。。。
sorted(array, key=) 这个特殊情况就这么两个主要用途，
按照length，或者按照index位置。

这里有点超纲。不记也行
