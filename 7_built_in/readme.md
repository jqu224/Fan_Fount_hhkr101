
⛵️：  
🌝：   
🌝：这不知道为啥每题默认python2，你注意一下，写之前把 mode 换成 python3  
 这里有个背景知识，尽管python3已经推出了快10年了，  但是还是有很多program没有改成3，还是2的写法。市面上用py2的code大概还有60%

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





[answer 1](#anchors-in-markdown)



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


