⛵️： ????     
🐍： !!!

。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

🐍：    
new term:     
pseudo code，伪代码，类似人们手写在纸上的那种，重在想象，你要相信它能run，不是真的code。     


。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
🐍：lambda is not important to analyst,     
   just go through my solution and call yourself happy     
   
   事实上，python对你也没有用。
   真正有用的是，numpy和pandas sql
   
   学python是为了下周用 pandas 和 numpy 操作 excel 表格
   
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
 ⛵️： 
 >> l = list(range(10))     
 >> l = list(map(lambda x:x*x, l))????     
🐍： !!！
   lambda x: x*x 意思是：for every x in the list，make x = x^2     
   
but, here we have 无名 function lambda     
lambda 和 for 不一样，for 需要 list 实例    
which allow us to （骗自己说）将来会有一个list，    
每个x都变成square of x了（画大饼你懂伐）    
   
   
    
   
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
   
⛵️： try后面的东西也看不懂？????     
🐍： !!!
try的意思是，lets try and okay to fail，譬如following code，z没有定义，本来print z会报错，但是try了以后。如果出错了，就让py跑except内的code：
    
```
>>> z   
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>   
NameError: name 'z' is not defined   
>>>    
>>>   
>>> try:   
...     print(z)   
... except:   
...     print(123)    
...   
123     
>>>    
>>> a
"aaaaaa"
>>> try:
...     print(a)
... except:
...     print(321)
...
“aaaaa”
```


。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
```
   try:
        username, url = email.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
```
⛵️： ValueError????       
🐍： !!!    
ValueError 是一种固定的error 形式，        
看到这种就去google：python valueerror        
    
继续将try，我知道怎么用，但是不会去用它。。        
因为我这个 analyst 工作的 project 是为了解决boss的问题，    
我的code是给自己写的，为了做数据分析，不是给用户或者别人的，      
接触不到try这种为了工程hardcore program而设计语句。     

但是，得知道怎么google，如果碰到了可以临时goole一下。不至于freak out     

 

。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

⛵️： if username.replace("-", "").replace("_", "").isalnum() is False:????     
🐍： !!!     
先replace“－” using empty char “”    
then replace ‘_’ using “”    
last，check is all elements in the parsed string （alpha or digit）    

```
>>> "1231=-2s.fdd=".replace("=","")
'1231-2s.fdd'
>>> "1231=-2s.fdd=".replace("=","  ")
'1231  -2s.fdd  '
```

isalnum() 之前学过。。。    

xxx.isdigit() check是不是1233..9    

xxx.isalpha() check是不是 abcd..z     
xxxx.isalnum()应该是both。。。    

overall：把username这个string 从左传递至右，     
依次: 先除去－再除去_ 最后看是不是alnum： alpha or digit      


>>> "12sdfdf323".isalnum()    
True    
>>> "12sdf+df323".isalnum()    
False    

  
为的是第二个rules，only contain alpha num    
Valid email addresses must follow these rules:    
 - It must have the username@websitename.extension format type.       
 - The username can only contain letters, digits, dashes and underscores.    
 - The website name can only have letters and digits.    
 - The maximum length of the extension is     ////
 
 
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

⛵️： 
 ```
def fibonacci(n):
    # return a list of fibonacci numbers  
    # # # # # # # # # # # #
    #  solution a
    if n == 1:
        return [0] 
    if n == 0:
        return [] 
    # from the explanation above: we need [0, 1] to get started,
    fib = [0,1]
    # for loop from the third element, till the end of list 
    for i in range(2,n):
        # fib += sum(fib[i-2:i-1])
        fib += [sum(fib[i-2:i])]
    return fib
     # # # # # # # # # # # #
    #  solution b
    fib = [0,1] 
    for i in range(2,n): 
        fib += [sum(fib[i-2:i])]
    return fib[0:n]
    
 if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
 ```
为什么这里的return的值都得是list????     
🐍： !!!    

1st，同一个defined function的return 要一致。make sense伐    
根据下文的main，需要一个list [0 1 1 2 3 5 ....]这样    
那么就把n = 0时，return设为[] empty list咯，    
再把n= 1时，return设为[0]咯    

为啥呢？因为我们斐波那契数列，    
是第一个第二个初始化得到的0和1，   
后面是计算的到的 1 2 3 5 8。。。。   
 

⛵️： main里面哪里说了需要一个list呢????      
🐍： !!!     
 print(list(map(cube, fibonacci(n))))     

map(a, b) a要求是一个function name譬如int(), 的话a 写int。。。    
b要求一个one element的东西，譬如 listp[]就是一个a list，符合要求     

所以，fibonacci ( ) 这个function 里面给他写个return list的话，是不是比较稳妥？     

如果写 return b1，b2 这就是return了两个东西，       
等于map(a, b1, b2)这下map三个argument input了，       
咱不熟悉，也许能过，但稳妥起见就不这么写了    

如果写 return【b1，b2】 这就是return了1个 list，      
等于map(a, b)这下map2个argument input了，     
  咱熟悉，肯定能pass，稳妥起见就这么写了     

还是map的问题，map是拿来一串element，      
用function a map成想要的样子       

。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
⛵️： ????     
🐍： !!!
>>> x = lambda x:x**2     
>>> b = list(map(x, [0,1,2,3,4]))    
>>> b     
[0, 1, 4, 9, 16]    

 

。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

⛵️：    
```     
>>> from fractions import gcd      
>>> reduce(gcd, [2,4,8], 3)    
1     
```    
????       
🐍： !!!     
GCD in PythonThe Greatest Common Divisor (GCD) is the largest integer         
 that evenly divides two numbers.        
 For example: gcd(10, 5) is 5 gcd(20, 8) is 4 gcd(9, 0) is 9.         
 Euclid noticed an efficient pattern for solving this problem back in 300BC,         
 which is known as Euclid's algorithm.     
 
  

```
>>> reduce(gcd, [20,4,8], 4)
4
>>> reduce(gcd, [20,4,8], 5)
1
>>> reduce(gcd, [20,4,8], 2)
2
>>> reduce(gcd, [20,4,8], 4)
4
>>> reduce(gcd, [20,4,8], 17)
1
>>> reduce(gcd, [20,40,80], 17)
1
>>> reduce(gcd, [20,40,80], 2)
2
>>> reduce(gcd, [20,40,80], 4)
4
>>> reduce(gcd, [20,40,80], 20)
20
>>> reduce(gcd, [20,40,80], 40)
20
```


⛵️：    
就是说 gcd(2,4,8) = 2以后     
gcd（2，3） = 1？？？     

🐍：sort of      


。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
     
⛵️： ????          
🐍： !!!       
   
def的时候写 def ress(a,b,c =100)代表着可以  不用写c：       
ress(1,2) a b 分别为1 和2，c传进去，就用默认的100       
ress(1,3,5) a b c分别为1 3 5，把5传入第三个argument的位置了，默认值就不用了     











⛵️：     
next() ????          
🐍： !!!
```
>>> a = iter([1,2,3,5])
>>> a
<list_iterator object at 0x000002B14A6ACB70>
>>> x = next(a)
>>> x
1
>>> x = next(a)
>>> x
2
>>> x = next(a)
>>> x
3
>>> x = next(a)
>>> x
5
>>> x = next(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> x
5
```


。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
 
⛵️： ????     
fraction(4,10) 是啥意思啊
🐍： !!!
一种特殊的type，fraction（1，3）表示三分之一。不用记。。。



THANK YOU~     
