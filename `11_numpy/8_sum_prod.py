https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy as np

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)

# solution a
b = np.sum(a, axis = 0)
print(np.prod(b))

# solution b
print(np.prod(np.sum(a, axis=0), axis=0))
