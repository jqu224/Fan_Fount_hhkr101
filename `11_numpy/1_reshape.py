https://www.hackerrank.com/challenges/np-shape-reshape/problem
  
import numpy as np

import_array = input().split() 
a = np.array(import_array, int)
# recall: pkg_name.method such as b_list = sorted(a_list) 
# usually apply the method to a_list and return to [b_list]
# however, method usch as  list_a.sort() 
# they return none and sort list_a

# nparray_name.shape  is a unique method 
# that count and return (row_num, col_num)

# here, the input is an 1d array (a vector) [1 2 3 4 5] 
# which has only one row and k columns
# a.shape gives us (num_of_col, )
cols, = a.shape

a_reshaped = np.reshape(a,(3,cols//3))
print(a_reshaped)
