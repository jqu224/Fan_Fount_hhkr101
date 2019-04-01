https://www.hackerrank.com/challenges/np-concatenate/problem
    
    
import numpy as np

a, b, c = map(int,input().split())

arrA = []
for _ in range(a):
    arrA += [list(input().split())]

arrA = np.array(arrA,int)

# or you can do it in a zhuangbility way
arrB = np.array([input().split() for _ in range(b)],int)

# solution a
# axis=1意思是沿着column左右拼接。
# axis = 0意思是row by row上下拼接
print(np.concatenate((arrA, arrB), axis = 0))

# solution b
# by default, axis = 0
print(np.concatenate((arrA, arrB) )) 



===============       NOTE      =====================
# by default, axis = 0
# column number must match to each other
A A
A A
A A
B B
B B

A is 3x2
B is 2x2


# axis = 1 means 
# row number must match to each other
A | B 
A | B
A | B

A is 3x4
while
B is 3x10
