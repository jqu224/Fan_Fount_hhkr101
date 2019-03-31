import numpy as np

a, b, c = map(int,input().split())

arrA = np.array([input().split() for _ in range(a)],int)
arrB = np.array([input().split() for _ in range(b)],int)

# solution a
print(np.concatenate((arrA, arrB), axis = 0))

# solution b
print(np.concatenate((arrA, arrB) )) 
