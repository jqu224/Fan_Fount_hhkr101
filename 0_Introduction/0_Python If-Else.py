#!/bin/python3

N = int(input())

# if  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird


# a % b  is the remainder of a divided by b
# 譬如第一个，if 是基数，print：
if N % 2 == 1:
    print("Odd")
elif N % 2  == 0:
    print("even")
    
# range(a，b,  c) 代表从a到b➖1得的数字，每一步公差为c
# 没有c，则默认公差为1，so range（0，5）就是 0 1 2 3 4
# also, for i in xxx，从xxx里按次序拿出所有的 element，in this case是🔢
for i in range(4, 10, 2):...    
        print(i) 
... 
>>> 4 
>>> 6 
>>> 8


# if 语句 下面的n行只要缩进都属于if判断
if N % 2 == 1: 
    print("Weird")
# elif代表，else if，means exclude from the above condition 
# 上面所有if之外的condition
elif N in range(2,6):
    print("Not Weird")
elif N in range(6,21):
    print("Weird")
elif N > 20:
    print("Not Weird")

# Following 🌰，永远不会执行elif，因为a若为8就被if这句吃掉了，会跳过这个elif和紧接着的所有elif
# if a in range(0,11):
#     pass
# elif a == 8:
#     pass
