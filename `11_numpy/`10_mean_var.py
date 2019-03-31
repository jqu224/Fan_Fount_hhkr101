https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
  
import numpy as np

# np.set_printoptions(legacy='1.13')
np.set_printoptions(sign=' ')

N, M = map(int, input().split())
_ = np.array([input().split() for i in range(N)], int)

print(np.mean(_, axis=1))
print(np.var(_, axis=0))
print(np.std(_, axis=None))
