import numpy as np

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr += [list(map(int, input().split()))]

a = np.array(arr,int)

# solution a
print(np.transpose(a)) 
print(a.flatten())

# solution b: same thing
print(a.T)
print(a.flatten())
