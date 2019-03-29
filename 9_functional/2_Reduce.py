https://www.hackerrank.com/challenges/reduce-function/problem



from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y : x * y, fracs) # complete this line with a reduce statement 
    return t.numerator, t.denominator
    
#     think about this:
    t = reduce(lambda x, y : x * y, [(1, 3), (4, 5), (29, 63)])
    
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)


#     #     #     #     #     #     #     #     #
# python code to demonstrate working of reduce()  
# importing functools for reduce() 
import functools 
  
# initializing list 
lis = [ 1 , 3, 5, 6, 2, ] 
  
# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,lis)) 
  
# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 


Output:

The sum of the list elements is : 17
The maximum element of the list is : 6
