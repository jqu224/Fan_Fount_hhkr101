---------------------
###range(10,1,2) -> 10 8 6 4 2
----------------------

print a，b是python 2
print(a, b)是python3

------
True or False boolean values
------





------
##True or False boolean values
------
```
>>> a = True
>>> a == 1
True
>>> a == 2
False
>>> a == 0
False
```
```
>>> a = 0
>>> a == True
False
>>> a == False
True
>>>反之亦可
```

--------------------------
for loop
--------------------------
上次的🌰，只是告诉你要小心，很多时候，return的答案不对，是因为code的时候，if case的<>=这些边界条件设计不对
但是呢，有时候，这个if里面的操作很复杂，就可以把这个anyvalue判断放在if后面用and连接，这样就不必做重复操作了
像这样的话，最好还是让if多判断一下，只有在这个char是alpha且没有翻过anyalphaetidcal牌子的情况下，我们才进去做这一长串的any = 1赋值
这里的重复操作是anylower = 1，也就是对把anylower变成true，这里比较简单跑一次也不碍事，所以and后面的可以不写
换句话说：
  这个if我进去玩过了，这次是我的第二次路过这个if isdigit == true，就不进去了
  
  －－－－－－－－－－－－－－－
  从最里面的()开始，再找()后面的[]，如果有的话，没有的话就找外面一层()，这就是python解码的时候的优先级
  －－－－－－－－－－－－－－
  hacker rank有个方便，你光标选中任意括号，她会提示你这个括号的另一半的位置，帮助你debug，找出你是不是漏掉括号了
  
  list_a = (str(i).rjust(w,' '),  str(oct(i)[2:]).rjust(w,' '),   str(hex(i)[2:].upper()).rjust(w,' '),  str(bin(i)[2:]).rjust(w,' ') 对了，这个其实不是list，你等于是制造了list_a == tuple
你需要lista = [a, b, c]方括号才行，
复习一下，tuple是不能改变内容的，list可以
```
>>> a = (1,2,3)
>>> a[0] = 11
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>啊！然而：
>>>
>>> b = [1,2,3]
>>> b[0] = 11
>>> b
[11, 2, 3]
```
  
  >>> a[2:1:-1]
(3,)
>>> a
(1, 2, 3)
  
  -------------------
  rjust ljust center
  --------------------
  ```
 不会考的，就是hackerrank广告
我也是试了半天才蒙出来的
 rjust ljust大概知道就行了
  (string_a).rjust(10) 就是string_a的字符靠右，用空格填满10个格子
  ______string_a
  (string_a).ljust(10) 就是string_a的字符靠左，用空格填满10个格子：
string_a________
  (string_a).center(10) 就是string_a的字符－居中－，用空格填满10个格子：
____string_a____
 
thickness = int(input()) 是input的数字呀
  好了，真的不考，男生也考不到这题。。。。」

```
