
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
