import math

# after you import math,
# you should be able to use 
#     c_num = complex(x,y)

>>> a = complex(2,3)
>>> b = complex(2,3)
>>> a
(2+3j)

# know you have two complex() object: a and b
# addition, subtraction, multiplication, and division
>>> a + b
(4+6j)
>>> a - b
0j
>>> a * b
(-5+12j)
>>> a / b
(1+0j)

# what you dont do
# div as int, find remainder
# we need to code these two by ourself if thats needed 
>>> a // b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't take floor of complex number.

>>> a % b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't mod complex numbers.


# # # # # # # # # # # # # # 
# following is the solution 
# # # # # # # # # # # # # # 
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary 
    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)
        
    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)
        
    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __truediv__(self, no):
        x = float(no.real ** 2 + no.imaginary ** 2)
        y = self * Complex(no.real, -no.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return Complex(real, imaginary)

    def mod(self):
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(real, 0)

    def __str__(self):
        
        # return '{0:04.2f}{1:+04.2f}i'.format(a.real, a.imag+0)
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
