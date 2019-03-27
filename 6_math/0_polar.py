# Enter your code here. Read input from STDIN. Print output to STDOUT


# solution a
import cmath
print(*cmath.polar(complex(input())), sep='\n')



from math import *
# solution b
# only work if the input are all positive
a, b = input().split("+")
b = b[:-1]
a, b = int(a), int(b)

print(sqrt(a**2 + b**2))
print(atan(b/a))

