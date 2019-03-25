### while_loop.md
while （）：只要括号里是成立的，就一直loop。
那么while True和while 1：一样，while 进入死循环 looping forever，因为True == True, while一直loop。
```
while True:
  print(12)
```
this will loop forever

while True：意义是有时候我们不知道什么时候停下：
while True：
    code：随机生成一个a == int
               如果随机的int 是0，我们break这个loop，
    if a ==0:
        break
这个while true代表了，当写while的这一行的时候，我们还不知道int的数值，等到int的数值产生了，并且是异常的时候，我们就break 这个loop

```
i = 1
while i < 10:
  print(blah blah)
  i *= 2
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
