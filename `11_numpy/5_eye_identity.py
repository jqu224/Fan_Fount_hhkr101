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
