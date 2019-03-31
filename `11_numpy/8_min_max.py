import numpy as np
The min along axis  =  
The max of  = 
n, m = map(int, input().split())
a = np.array([input().split() for _ in range(N)],int)
print(np.max(np.min(a, axis=1), axis=0))

