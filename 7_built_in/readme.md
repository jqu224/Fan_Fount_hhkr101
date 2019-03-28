
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
```

Q1: which one is correct?
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


