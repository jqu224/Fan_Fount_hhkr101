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



=======================================================
注意这个逗号，
>>> a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).shape
>>> a
(9,)
>>> a, = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).shape
>>> a
9

>>> a, = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).shape 注意a后面的逗号，要这样才能脱掉括号
>>> a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).shape[0]
a both == 9

这是一个特例。
1d是一个 n by 1 的array，
她的 shape return是 number 和空。

2d 的 shape return 是 row 和 column
