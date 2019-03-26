提问 len可以用在string list上 可以用在tuple set 上嘛
---------
```
if len(set_a - set_b) == 0:   
              print(True)  
          else:  
              print(False)  
```


```
list可以+=任意的东西，+=[[list]] +=int +=float += ["string"]都可以
>>> a+=[[1,2,3]]
>>> a
[1, 23, 3, [1, 2, 3]]
```
```
>>> a,*b = input().split()
1232 343434 45645
>>> a
'1232'
>>> b
['343434', '45645']
 
>>>
>>> a,*b = input().split()
12 323
>>> a
'12'
>>> b
['323']

这里用了*，没空格不报错，
不然python会：呀说好的一个给a一个给b，你只写了一个，我只好写个error给你了

>>> a, b = input().split()
123
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 2, got 1)


```
```
union: a bing b
>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}

>>> x1.union(x2)
{'foo', 'qux', 'quux', 'baz', 'bar'}

>>> x1 | x2
{'foo', 'qux', 'quux', 'baz', 'bar'}

```


```
intersection in both a and b
>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}

>>> x1.intersection(x2)
{'baz'}

>>> x1 & x2
{'baz'}

>>> a = {1, 2, 3, 4}
>>> b = {2, 3, 4, 5}
>>> c = {3, 4, 5, 6}
>>> d = {4, 5, 6, 7}

>>> a.intersection(b, c, d)
{4}

>>> a & b & c & d
{4}
```

```
difference
only exists in x1
>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}

>>> x1.difference(x2)
{'foo', 'bar'}

>>> x1 - x2
{'foo', 'bar'}

>>> a = {1, 2, 3, 30, 300}
>>> b = {10, 20, 30, 40}
>>> c = {100, 200, 300, 400}

>>> a.difference(b, c)
{1, 2, 3}

>>> a - b - c
{1, 2, 3}


>>> b = set([1,2])
>>> a = set([2,4])
>>> a - b
{4}
```

```
symmetric_difference
a ^ b = (a - b) | (b - a)
>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}

>>> x1.symmetric_difference(x2)
{'foo', 'qux', 'quux', 'bar'}

>>> x1 ^ x2
{'foo', 'qux', 'quux', 'bar'}

>>> a = {1, 2, 3, 4, 5}
>>> b = {10, 2, 3, 4, 50}
>>> c = {1, 50, 100}

>>> a ^ b ^ c
{100, 5, 10}
```





