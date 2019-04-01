https://www.hackerrank.com/challenges/np-eye-and-identity/problem
    
import numpy as np

# # # # # GOAL:
# take in the N, M values
# print a NxM (pronounced as N by M) eye matrix

# hackerrank is silly, it's using an old print_option 
# which adds one space char in front of each [cell] in the matrix
np.set_printoptions(legacy='1.13')

n, m = map(int, input().split())

# solution a
if n == m:
    print(np.identity(n))
else: 
    print(np.eye(n, m, k = 0))
    # # or simply
    # print(np.eye(n, m))

# solution b
# without np.set_printoptions(legacy='1.13')
print(str(np.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))


=============================================================================
>>> np.eye(3,5,1) 也是可以的，不推荐这么写（只是了解一下，以防看不懂别人的 code）。
>>> np.eye(3,5,k=1) 这样写就好，容易 debug
