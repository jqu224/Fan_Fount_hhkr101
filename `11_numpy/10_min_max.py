https://www.hackerrank.com/challenges/np-min-and-max/problem
  
import numpy as np

# The min along axis=1 => gives a vector: a vector is a 1d array  
# The max of vector => single value
n, m = map(int, input().split())
a = np.array([input().split() for _ in range(N)],int)

# solution a
vec = np.min(a, axis=1)
print(np.max(vec, axis=0))

# solution b
print(np.max(np.min(a, axis=1), axis=0))
