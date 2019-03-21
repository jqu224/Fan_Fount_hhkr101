```
>>> a = "1234567"
>>> b = "abcdefghijk" 
  解：
>>> x = [i+j for i, j in zip(list(a),list(b))]
>>> x
['1a', '2b', '3c', '4d', '5e', '6f', '7g']
>>> "".join(x)
'1a2b3c4d5e6f7g'
>>> answer = "".join(x) + b[len(a):]
>>>answer

'1a2b3c4d5e6f7ghijk'
```
