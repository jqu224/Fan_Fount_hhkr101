
```diff
if not print(1):
    print(123) 
print("------😳------")
if print(1):
    print(123) 
    
⛵️ output:
1
123
------😳------
1

⛵️ :
>>> a = print()

>>> a
>>>
print() -> print a empty line


>>> for i in range(4):
...     a += [int(input())]
...
1
3
5
7
>>> a
[1, 3, 5, 7]

这个括号 a += [xxx] 是固定用法，代表把 [ ] 里的 xxx 当作一个element +入左边的list的末尾

>>> a += 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable

# 如果是 list
>>> a += [[1232]]
>>> a += [[11,22]] 
>>> a
[1, 3, 5, 7, [1232], [11, 22]]

```

List
```
>>> a
[1, 3, 5, 7, [1232], [11, 22]]
>>> a[0]
1
>>> a[-1]
[11, 22]

>>> a[-2]
[1232]

>>> a[-2] + a[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "int") to list
>>> a[2] + a[0]
6
```


```
>>> a[-2] + a[-2]
[1232, 1232]
以及上面这样a[-2] == [1232] 倒数第二个位置是一个sub list，这sub里面是 1232
python认为你要concatenate，连接两个list，于是py把这两个sub list放在一个list里return给你了。


刚才没用variable接收return的value,

>>> b = a[-2] + a[-2]
>>> b
[1232, 1232]
这样你就接收到了

```
```
a = [] list
a = () tuple
tuple () 和 list [] 
存 save 的方法基本一样，
调用 call 也极其类似，都可以 print( list[0] )，
只是前者不能改动 immutabl，unable to be changed.
```
