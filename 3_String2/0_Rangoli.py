def print_rangoli(size):
    # your code goes here
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    len_0 = size - 1
    lines = [(alpha[len_0:(len_0-i-1):-1] + alpha[size-i:size]) for i in range(len_0)]
    lines = ["-".join(i).center(size*4-3, "-") for i in lines] 
    
    print("\n".join(lines + ["-".join(alpha[size-1:0:-1] + alpha[:size])] + lines[::-1]))

    # join是用－连接e d c d e内部，center是把头尾用－补全

    # 先看join括号里的：(lines + ["-".join(alpha[size-1:0:-1] + alpha[:size])] + lines[::-1])
    # lines是：
    # --------e--------
    # ------e-d-e------
    # ----e-d-c-d-e----
    # --e-d-c-b-c-d-e--
    # 加上 一行满的：e-d-c-b-a-b-c-d-e
    # 在加上反lines[::-1]
    
#     ["-".join(alpha[size-1:0:-1] + alpha[:size])]
# 先翻个身alpha[size-1:0:-1]：edcb,没有a 
# 再alpha[:size])：加上abcde
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

-----------------
    
Sample Input

5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

    lines = [(alpha[len_0:(len_0-i-1):-1] + alpha[size-i:size]) for i in range(len_0)]
    这一句：建立len_0这么多行的 list，把这n行 list 赋予lines
下一句就是打开lines，把里面每一行join起来，
    
    
    lines是 [[1,2,3] [11,22,33] [44,55,66]]
temp = []
for i in lines:    
         temp += "-".join(i)
       这里每一个 i 分别是：[1,2] 和 [11,22] 【44，55，66】
for结束：得到了temp == 【【“1－2”】【“11－22”】【“44－55－66”】】

temp =【"-".join(i) for i in lines】就是上面的装b写法，
意思是create a list each element is joined result of each element in lines 

>>> b
[11, 2, 3]
>>> b += ["-",'=']
>>> b
[11, 2, 3, '-', '=']
list可以+= 就等同于 list_a.append(123)

lines = [x**2 for x in numbers] 
GG不推荐这样子写，只是需要你会看这种装b的写法，有些时候也是有方便的。以后会说di


>>> a
(1, 2, 3)
>>> ab = [x**2 for x in a]
>>> ab
[1, 4, 9]





