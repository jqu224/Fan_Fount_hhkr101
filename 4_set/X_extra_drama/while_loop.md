### while_loop.md
while （）：只要括号里是成立的，就一直loop。
那么while True和while 1：一样，while 进入死循环 looping forever，因为True == True, while一直loop。
```
while True:
  print(12)
```
the code above will loop forever
```
while True：意义是有时候我们不知道什么时候停下：
while True：
    code：随机生成一个a == int
               如果随机的int 是0，我们break这个loop，
    if a ==0:
        break
这个while true代表了，当写while的这一行的时候，我们还不知道int的数值，
等到int的数值产生了，并且是异常的时候，我们就break 这个loop
```
```
while True:
    password = input('请输入您的密码：')
    if d[name] == password:
        print('进入系统')
        break
    else:
        print('您输入的密码不正确，请重新输入')
        continue
譬如这里我们要输入正确密码，
如果输入正确，就进入系统（停掉这个while loop跑别的代码去了）
如果输入错误，要用户一直输入 while 就一直looping
continue可以不写        
```
```
i = 1
while i < 10:
  print(blah blah)
  i *= 2
  
解：
i = 1
while (i ==1) <10
 blah 
 i => 2
while (i ==2) <10
 blah
 i => 4
while (i ==4) <10
 blah
 i => 8
while (i ==8) <10
 blah
 i => 16
while i == 16 <10 不对啦！while loop就此停止

>>> i = 1
>>> while i < 10:
...     print("nai xin dian")
...     i *= 2
...
nai xin dian
nai xin dian
nai xin dian
nai xin dian
```
same thing as the second while loop 



```
i = 1
while True:
  print(12)
  if i == 10:
    break
  i += 1
```
u can use a break 中断 to stop the while True loop
(here i used i as a counter)
