# Enter your code here. Read input from STDIN. Print output to STDOUT

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
