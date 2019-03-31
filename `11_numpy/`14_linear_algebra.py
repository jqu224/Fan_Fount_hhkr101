import numpy as np
from numpy import linalg

numpy.set_printoptions(legacy='1.13')  # important

n=int(input())
a=np.array([input().split() for _ in range(n)],float)

# a
print(np.linalg.det(a))

# b
print(linalg.det(a))
