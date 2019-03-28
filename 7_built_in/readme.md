
⛵️：  
🌝：   

======================================     
🌝：这不知道为啥每题默认python2，你注意一下，写之前把 mode 换成 python3      
       
 这里有个背景知识，尽管python3已经推出了快10年了，   
 但是还是有很多program没有改成3，还是2的写法。市面上用py2的code大概还有60%     
 恩，but its a sinking ship，will be gone

```
print 123 for py2       
print(123) for py3      
and py3 used some modern packages 
such as [import xxx] at the start of your code... 
you may have seen them already, 
```
```
input().split() 是把 input() 从输入端拿到的string 
按照默认的 sep = “ ”变成 list

>>> b = input().split()
123abc 234
>>> b
['123abc', '234']
>>> a = input()
123abc 234
>>> a
'123abc 234'
```

```
py3是从左之右 从里至外，依次执行你的code的。
譬如s =  input().split() 这句话，

先做 input() 拿到 string

==============如果不写 .split() 那么s就是你输入的string了呀 譬如“abc  123”(注意空格)===========
再做 .split() 分成一个list 譬如【“abc”， “123”】就成了2个element的 list
```

```
⛵️： x, ans = map(int, input().split())这个 run 出来就是【“1”，“4”】对么 
🌝：  x, ans = map(int, input().split())这个 run 出来是x= 1，ans =4 ,
       你已经把每个element都map成了int了，然后你又分配给了x和ans，
       每个都等于一个int， 是 x=1，ans=4
       x, ans = map(int, input().split())这个 run 出来是x= 1，ans =4 ,
       你已经把每个element都map成了int了
```
```
⛵️： poly = input(), print(eval(poly))??? 
🌝：  因为我们只需要把输入的string原封不动地eval（）就好了，
       譬如我们写：“x**2 + x” 那么poly = input() 
       这时候poly == “x**2 + x”（由于这个x已经在前几行定义过了,假设x = 3）
       现在来执行 eval(ploy) 就是 3**2+3 = 12
       
       多项式结构会变譬如x**3 + x**2 + x + 或者 x**12 + 123，
       但是，x不变，所以我们先把第一个数定义为，
       第二个数是用来和eval的result比较的，可以随便命名
```
```
⛵️： x, ans = map(int, input().split())这个 run 出来就是【“1”，“4”】对么 
🌝：  
>>> a, b, c = [1,2,3] 这里是list的拆分
>>> a
1
>>> b
2
>>> c
3
>>> a, b, c = (1,2,3) 这里是tuple的拆分
>>> a
1
>>> b
2
>>> c
3
>>> a, b, c = {1,2,3} 这里是set的拆分
>>> a
1
>>> b
2
>>> c
3

等式左边 a, b, c = 右边 
这意思是把右边的 a series of things 拆开来，让a连接第一个，b连接第二个


那为啥map也可以呢？事实上，map()的结果是 a （series） of int or float or ... 
map()这个function他return的value也是可以数的element，
但是外面的大括号没有定义。不知道是不是list还是tuple还是set，前两天讲过一点

有一群鸡蛋，不知道放哪里。放篮子里就是 list 
放冰箱里就是 tuple，啥也不放，也没关系，因为有index，可以摘出来。
as long as you can locate them

不打[] （） ｛｝的话，就是map return value 没穿衣服。。。
啥也不是。是一串 map（） 过得（对象 object）。你可以理解为element）

鸡蛋还是那个鸡蛋，list 和tuple是他们的容器，装饰用的。

a,b = list_x
等于a = list_x[0]
b = list_x[1]
⛵️： 给鸡蛋起名字？
🌝：对，下次可以单独叫 b 出来聊聊
```


```
⛵️： 这print里面有一个and 就能print出两行？」 print(a<2 and a<10)

🌝：  一行呀，and左边是个判断shi，右边也是判断式，
       譬如print(a>2 and a<1)，只有a又比2大又比1小，才会print（True），这里就是print False了
       左边式子：all([x>0 for x in list_a]) 
        右边shi子：any([str(x) == str(x)[::-1] for x in list_a])
 ⛵️： and 就是要左边且右边 才是true  哪边不对都是false
        
🌝：  or 就是两者任意true则true，
       a or b or c呢？就是三者取1 true则true，
       a or b and c呢？
       先b and c 再和a比。
       这里不合理。为了保险起见，（a or b） and c就好了
```
```
 ⛵️： 为啥是all([])
🌝： 
>>> all(【True, False】)
False
>>> all((True, True))
True都可以哎，只要是a series of element形式就行

all(xxx) is checking the element inside xxx one by one
all([x>0 for x in list_a]) 这个方括号
是为了[x>0 for x in list_a] 写的,不的话,x>0 for x in list_a就不是list了

>>> [x for x in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


>>> x for x in range(10)
  File "<stdin>", line 1
    x for x in range(10)
        ^
SyntaxError: invalid syntax

```
```
⛵️： 
🌝：  


>>> x [for x in range(10)]
  File "<stdin>", line 1
    x [for x in range(10)]
         ^
SyntaxError: invalid syntax


>>> [x for x in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
固定搭配.【】里面意思是，for这些符合条件的数，用【】建立一个 list 来给他们统统套起来


[x for x in range(100) ] 就是 x在0到99
[x for x in range(100) if x %2 == 0] 就是 0 2 4 6 8。。。。98

```
```
⛵️： 这个rstrip是什么
🌝：  string rstrip() by default, remove all 首尾出现的spaces .
string.rstrip("x") remove all x's from shou wei

str = "     this is string example....wow!!!     ";
>>>print str.rstrip()
this is string example....wow!!!


str = "88888888this is string example....wow!!!8888888";
>>>print str.rstrip('8')
88888888this is string example....wow!!!

x chars have been stripped from the end of the string (default whitespace characters).
```
```
⛵️： lambda 是什么？是那个希腊符号么
🌝：  lambda 就是一个阅后即焚的无名函数。风云看过伐？无名剑法，一哈一哈哈。憋了很久，自以为无敌，秀了3秒，出来就死了的那个
yeap,显得高级
当你需要一个无名函数的时候，就取这么名字，py就懂了，
噢装b了要，而且就在这1行装b，以后都不用了，
以后再设lambda又是一个新的，阅后即焚的 one line only 的lambda

表示我是无名，你这三周的py世界里里出现过的最高级的东西

```
```
⛵️： sorted 为什么不能直接print sted
🌝：  
因为sorted的return  是 list，本题要求print string 还得one line after another
>>> a = sorted([11,2,3])
>>> print(a)
[2, 3, 11]
>>> print(*a)
2 3 11
>>>
>>> a = sorted([[11,2,3],[3,4,5]])
>>> a
[[3, 4, 5], [11, 2, 3]]
>>> print(*a)
[3, 4, 5] [11, 2, 3]
```
```
⛵️： 2d arry是什么
🌝：  
[1,2,3]
这是1d array，一维数组，

2d array是
【【1，2，3】，

【3，4，5】，

【512，23，5】】
2d array，二维数组，有横向有纵向

🌝： 然后变成string 就
三个list ["1" "2" "5】,【"2" "3" "4"】.【 "3" "4" "5"】
再" ".join变成
第一个string"1 2 3", 第二个string“2 3 4”, 第三个string“3 4 5”
“\n".join 变成
1 2 3
2 3 4
3 4 5
en

```
⛵️：再join 成 [1 2 3] ？
🌝：  不对，是join 成 “1 2 3”

```

create a set:
1a)  head = {}
1b)  head = ()
1c)  head = set()

print the set
2a)  print(sorted(list(head)))
2b)  print((list(head).sort()))
```





[Answer 1:](#anchors-in-markdown)



```
eval(string) take in the string and evaluate it,
s = "print(123)"
eval(s)
-------
gives u the same thing as print(123)
123

⛵️：为什么要有这个东西的存在呢
🌝：恩,这里就可以用到...
```
```

create a set:
1a)  head = {}
1b)  head = ()
1c)  head = set()

print the set
2a)  print(sorted(list(head)))
2b)  print((list(head).sort()))
```
```

create a set:
1a)  head = {}
1b)  head = ()
1c)  head = set()

print the set
2a)  print(sorted(list(head)))
2b)  print((list(head).sort()))
```
```

create a set:
1a)  head = {}
1b)  head = ()
1c)  head = set()

print the set
2a)  print(sorted(list(head)))
2b)  print((list(head).sort()))
```
```

create a set:
1a)  head = {}
1b)  head = ()
1c)  head = set()

print the set
2a)  print(sorted(list(head)))
2b)  print((list(head).sort()))
```
```

create a set:
1a)  head = {}
1b)  head = ()
1c)  head = set()

print the set
2a)  print(sorted(list(head)))
2b)  print((list(head).sort()))
```







Answer 1:(#anchors-in-markdown)
---------------
1c & 2a

2b will print(None) 
since a.sort(): sort and replace a but no return value


