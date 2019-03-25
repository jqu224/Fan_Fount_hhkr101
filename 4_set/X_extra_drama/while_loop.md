while_loop.md
while （）：只要括号里是成立的，就一直loop。
那么while True和while 1：一样，while 进入死循环 looping forever，因为True == True, while一直loop。
```
while True:
  print(12)
```
this will loop forever


```
i = 1
while True:
  print(12)
  if i == 10:
    break
  i += 1
```
u can use a counter to stop the while True loop
(here i used i as a counter)

```
i = 1
while i < 10:
  print(blah blah)
  i *= 2
```
same thing as the second while loop 
