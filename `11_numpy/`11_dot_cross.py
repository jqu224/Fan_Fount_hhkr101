https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy

n=int(input())
a = numpy.array([input().split() for _ in range(n)],int)
b = numpy.array([input().split() for _ in range(n)],int)
m = numpy.dot(a,b)
print (m)
