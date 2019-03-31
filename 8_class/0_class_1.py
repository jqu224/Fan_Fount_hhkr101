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



这里的class定义了一个（类），(类别) 的意思，和def很像，但是放在def外面，
如果说def是一种操作，譬如
def eat（a）：让a去吃饭

class chinese（a）：
表示的是定义一个object a ，
而a内置的defined function包含各种callable的可能性：

譬如
class chinese(object):
  blah = 0
  
  def __init__(self, name):
    self.name = name
  def eat(a):
    print(吃吃吃)
    
  def loud(a):    
    talk talk talk    
  
  @classmethod 
  def get_no_of_instance(xxx):
      chinese.blah = chinese.blah + 1
      return xxx.blah
    
  @staicmethod 
  def get_no_of_instance(xxx):
      return xxx.no_inst
然后初始化：
>>> a = chinese("fan")

你可以用
>>> a.eat()
print: 吃吃吃
  
  
来让a吃饭了
a.eat()
output:
print: 吃吃吃
  
  
／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／／
用的时候
#   这里呢，__xxx__ 表示xxx是一个内部函数，譬如 
a，b = 1, 3
事实上a和b都是int object，自带+-*/ % //法，这些都是__add__ __sub__ __div__ etc.
we have these 预先写好的 function of class (int)，
因此才可以写 a + b， a - b（具体看下文 solution 理解）

solution 的 code 就是让你重新写一遍这些内置函数
－－－－－－－－－－－－－－－－
self 代表这个 this object 自己's stuff，不算传入的argument

# 这里init是用来初始化的，譬如 
class里的init有写：
def __init__(self, waha):
  self.waaa = “waha”
  
而 we initialize an object by using: 
>>> a = chinese(arg1)
  
  那么，这个a就把arg1 take in成了他的waaa这个特征了。
////////////////////////////////////////////////////

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
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
