import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    
    # solution a
    return numpy.array(map(float,arr[::-1]))
    
    # solution b
    return numpy.array(arr[::-1],float)


arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)
