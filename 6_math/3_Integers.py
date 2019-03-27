# Enter your code here. Read input from STDIN. Print output to STDOUT
power mod, 
two function with different input arguments: 2 arguments or 3 arguments
if 2 arguments:   pow(a,b) == a**b == a^b
with 3 arguments:  pow(a,b,w) == (a**b)%w == mod(a**b, w)
	
	
# solution a
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a**b + c**d)

# solution b
a,b,c,d = (int(input()) for _ in range(4))
print (pow(a,b)+pow(c,d))




...................................
这个solution b是抄的，意思是 for loop执行4次，
每次int(input)一个数，这样等号右边变成了一个tuple，里面四个int，
这时候执行等号，把 a b c d 分别指向右边这tuple里的第1234个数


如果是a=(int(input()) for I in range(4))，
那么是先执行右侧，先take 4个int，放到()tuple里，
此刻这个tuple还没名字，最後执行等号，a指向这个无名tuple

a=(int(input()) for I in range(4)) ==== a=(int(input()) for _ in range(4)) 
you can use [i] [_] or [m] [name] [waht] [anything] just dont use the same name as [a]



⛵️：is this okay?
for _ in range(4):
	a,b,c,d = int(input()) 

-  nope
这个逻辑就错了。 = int(input()) 这个等式的右边只有一个return value 
which is a single int。只能赋予一个variable name


这里的关键是你需要4个variable，其实如下也行：
a = []
for _ in range(4):
    a += [int(input())]
用的时候call by a[0] a[1] a[2] a[3]就好了


for只能和前几天做的一样，放在式子上方，或者今天这样放在后侧，
2者 没有区别，建议最好都放在上方外面，不要和等式挤在one line 里

a, b, c, d = (1,2,3,4) means unpack the right hand side 
and map them to a b c d these 4 variables. NOTE! must be same length
