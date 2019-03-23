n = int(input())   #  索要一个input，然后把它赋值给n这个变量。
s = set(map(int, input().split()))  #  索要一个input，然后把它赋值给 s 这个 string。
# 第 4 和 5 两行, 等于 第七行一行
M = int(input())   #  索要一个input，然后把它赋值给M这个变量。
for i in range(M):
    
for i in range(int(input())):
    cmmd, *num = input().split()
    if cmmd == "pop":
        s.pop()
    elif cmmd == "remove":
        s.remove(int(num[0]))
    elif cmmd == "discard":
        s.discard(int(num[0]))

print(sum(s))


========================================
题目规定要take in 4个 input，分别是：
一个int as n
一个list as s
一个int as 无名value： x，传入 for range（）
x 一个list。

所以对症下药。写四个input（）

for i in range(int(input())):意思是：
1：int( input()) takein 一个int，
2：然后create a loop range(n): 0, 1, 2, N-1
3：之后，开始loop：i为 0 －>1 ->2 。。。N－1 
input()只运行了一次，第1步之后，不再take in input（）
========================================

跑了N次的：    cmmd, *num = input().split()
cmmd就是第一个argument，remove 或者pop或者discard指令。
为啥要用*num呢？
因discard 和remove是要 discard（value）和remove（value），而pop（）是没有的

commd, *num means 

假设 ”aaa  bbb ccc "回车
第一个string赋值给cmmd
第二第三个如果有，就变成list给num
只有第二个string”aaa  bbb"回车：那么num就是string。
如果第二个也没有”aaa"回车，那就是num为空。并且告诉python，不要大惊小怪，code没有错

没有*，代表这一行输入，有且只有2个string

========================================
set_name.pop（）就是pop出一个element
对，还有element就pop，没有的话 报错。

setname.pop()
setname.remove(value)

hackerrank的例子是python2：

 print a, b
你用的是python3
print(a,b)



为啥呢？因为所有的题哦都是死板的写好的，题目的input是固定的，
int m
list of xxxx consists of m int
int n
list of zzzz consists of n int

为了解题，配合他，假装在第一次拿进m。地3次拿进n 两个int

已知：先跑来一个int 10告诉你第二行有10个数字，第三行再跑来int 20告诉你第四行有20个数字
那么，我就要先take in第一行的 10
再take in 第二行as list
再take in 第三回的 20
最后take in第四行的 list
不能直接取 list a和list b的／／／／


譬如hello！ next list len is： 
输入int：10 
结果
第二行输入：1 2 3 5 6 放入s
就回车了

这个时候 第一行这个就可以用来检测后面的是不是输入够了
if len(s) == n:
    print("yes")
else:
    print("no")
    
这里会print： no


    
    
    






