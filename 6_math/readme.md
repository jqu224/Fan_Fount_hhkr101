
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

>>> a += 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable

>>> a += [[1232]]
>>> a += [[11,22]]
>>> a
[1, 3, 5, 7, [1232], [11, 22]]

```

