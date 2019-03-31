# solution 1 , importing pkgs
# here numpy is a package that consists of pre-defined functions
# that we can use to achieve diff [goals]
import numpy
def arrays(arr):
    # complete this function
    # use numpy.array
    
    # solution 1.a
    return numpy.array(map(float,arr[::-1]))
    
    # solution 1.b
    return numpy.array(arr[::-1],float)

# solution 2 , aliasing
# by aliasing, we can use nicknames to call the package
import numpy as np

def arrays(arr):
    # complete this function
    # use numpy.array
    
    # solution 2.a
    return np.array(map(float,arr[::-1]))
    
    # solution 2.b
    return np.array(arr[::-1],float)

# solution 3 , from -xxx- import  -yyy- 
# * means unpack [all of the sub packages in -xxx-]
# so that we could use numpy.array as array (python already knows you are using array)
# but this particular method could be confusing, 
# since you may have multiply packages which consists of the same subpkg [array] 
# and they could be functional differences between these different [array] packages
# for this reason, you may wanna keep using the prefix names such as np.array(), kp.arary().. pp.array() 
from numpy import *

def arrays(arr):
    # complete this function
    # use numpy.array
    
    # solution 3.a
    return array(map(float,arr[::-1]))
    
    # solution 3.b
    return array(arr[::-1],float)

# # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # main functions # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # 

arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)
