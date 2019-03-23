这题怎么做的不重要，w这行是为了下文对齐用的，这里重要的是进制

def print_formatted(number):
    # your code goes here 
    w=len(bin(number)[2:]) 
    for i in range(1,number+1):
        print (str(i).rjust(w,' '),
            str(oct(i)[2:]).rjust(w,' '),
            str(hex(i)[2:].upper()).rjust(w,' '),
            str(bin(i)[2:]).rjust(w,' '),sep=' ')
        
#         那可不可以 
        list = (str(i).rjust(w,' '),  str(oct(i)[2:]).rjust(w,' '),  
                      str(hex(i)[2:].upper()).rjust(w,' '),  str(bin(i)[2:]).rjust(w,' ') 
#                 然后
        print “ ”.join(list)
                
                
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
    ============================
   
正常是 decimal 10进制，每一位由0到9组成， 9+1进位成10
binary是 2进制，每一位由0到1组成， dec(2) = 1+1进位成 10，dec(3) －> bin(11); 4-> bin(100)以此类推
octal是 8进制，每一位由0到7组成， 8 = 7+1进位成 oct(10)，dec(15) －> 1*8 +7 oct(17); 17->2*8+1 oct(21) 以此类推
hex 16进制比较复杂，0到F，是十进制的0到6


hex:为什么要abcdef呢？因为需要16个single char，0－9只有10个，不够了，借abcdef来用用a是10 b 11 c 12 d13 e14 f是15，
举例：16进制的hex 1A -> 1*16 + A 是10 －>等于十进制的 26 啦

心算算法的话 bin(99) 呀，要是2^7就成了128了，
那只能先取64 2^6 余35，下一个2的n次方是 32，余3 呀！3减去 2^1 余 1 呀！1就是2^0 也就是1100011啦


举例：16进制的hex AA -> 第二位上是a = 10 *16^1 + 第一位是 A = 10 －>等于十进制的10×16 + 10 =  170啦

hex: AAA = (10 × 16²) + (10 × 16¹) + (10 × 16⁰) = 2730
    
    公式：sum(当前数字×进制^当前位数)
    
    譬如：10进制：876 = 第2位8 x 10^2 + 第1位 7 x 10^1 + 第0位 6 x 10^0 = 800 + 70 + 6
    
    譬如：16进制：876 = 第2位8 x 16^2 + 第1位 7 x 16^1 + 第0位 6 x 16^0 ....以此类推
    
    进制这个概念蛮重要的。
    
    
    ==============
 


10 // oct= 1 余 2
这时候不用被8除了，因为2<8了
除了1次，0+1 一共2位 第一位就是 1 
所以oct(1000) = 12

1000 // hex = 62.5
62.5 // 16 = 3.9// 这时候不用被16除了，因为<16了
除了两次，0+2 一共三位 1000 = 3.9...* 16^2 第一位就是 3 
1000 － 3×16×16 = 232
232／16 = 14 余 8  已知14 == E
所以 hex(1000) = 3E8

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001     
题目要求对其，这里 w=len(bin(number)[2:]) 
是把binary of number的长度数出来，下面用来rjust ljust 对齐

======


w=len(bin(number)[2:]) 数一下最长length会是多少呢？
先运行bin()意思是把括号里面的10进制转换为2进制，得到：0b10001.,
然后bin()[2:0]从第三位开始取得到10001 
从第三位开始才是数zi，hex是 0x___ oct是0o___ binary是 0b____，


再套一个len（）得到5这就是最长的输出的长度了


bin(number)[2:]  呢是因为从第三位开始才是数zi，hex是 0x___ oct是0o___ binary是 0b____，
我们这里要求只把数字打印出来，所以从第三位开始取

>>> bin(100)
'0b1100100'
>>> hex(100)
'0x64'
>>> oct(1000)
'0o1750'


str(oct(i)[2:]).rjust(w,' '),举例来说，这个8进制，居右对齐，剩余的字符空间用空格 ' ' 填充
譬如   17    21    11 10001  
事实上你要的是 十进制5个字符 + “ ” + 8进制5个字符 + “ ” + 
16进制5个字符 + “ ” + 2进制5个字符 
那么print的就是： 3个空格+ str(17) + " " + 3个空格 + str(21) + " " + 3个空格 + str(11) + " " + 0个空格 + str(10001) 

所以10.rjust(5,' ')是？
1和0两个字符居右靠旁边，然后用3个空格填满左边，
overall占了5个格子

所以5的意思是overall五个格子？不是加五个空格？
对的，注意不能10.rjust(5,' ') 需要 “10”.rjust(5,' ')

>>> "10".rjust(10," ")
'        10'
>>> 10.rjust(10," ")
  File "<stdin>", line 1
    10.rjust(10," ")
           ^
SyntaxError: invalid syntax
invalid syntax就是python想告诉你，你写的我看不懂
请尊重规范，同理：“-”.join(list) 或者"1".join(list)都行，
就是不能 1.join(list)

这个是因为要用sep字符把他们连起来：print (str(i).rjust(w,' '),  str(oct(i)[2:]).rjust(w,' '),   str(hex(i)[2:].upper()).rjust(w,' '),  str(bin(i)[2:]).rjust(w,' '),sep=' ')

把这长串简化一下：print(a,b,c,d, sep=" ")也就是 a b c d用空格分开的意思

>>> print(1,2)
1 2
>>> print(1,2, sep="-")
1-2


str(oct(i)[2:]).rjust(w,' '),举例来说，这个8进制，
居右对齐，剩余的字符空间用空格 ' ' 填充


譬如   17    21    11 10001  
事实上你要的是 十进制5个字符 + “ ” + 8进制5个字符 + “ ” + 
16进制5个字符 + “ ” + 2进制5个字符 
那么print的就是： 3个空格+ str(17) + " " + 3个空格 + str(21) + " " + 3个空格 + str(11) + " " + 0个空格 + str(10001) 

所以10.rjust(5,' ')是？
1和0两个字符居右靠旁边，然后用3个空格填满左边，
overall占了5个格子


======

所以align只能align string是么 不能align int
>>> "10".rjust(10," ")
'        10'
>>> 10.rjust(10," ")
  File "<stdin>", line 1
    10.rjust(10," ")
           ^
SyntaxError: invalid syntax
  invalid syntax就是python想告诉你，你写的我看不懂  
    
    
    这个是因为要用sep字符把他们连起来：print (str(i).rjust(w,' '),  str(oct(i)[2:]).rjust(w,' '),   str(hex(i)[2:].upper()).rjust(w,' '),  str(bin(i)[2:]).rjust(w,' '),sep=' ')

把这长串简化一下：print(a,b,c,d, sep=" ")也就是 a b c d用空格分开的意思

 
Q: 可不可以 list = (str(i).rjust(w,' '),  str(oct(i)[2:]).rjust(w,' '),   str(hex(i)[2:].upper()).rjust(w,' '),  str(bin(i)[2:]).rjust(w,' ') 然后print “ ”.join(list)
 
应该是可以的吧














    







