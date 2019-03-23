# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input()) 
list_a = set(map(int, input().split()))

m = int(input())
list_b = set(map(int, input().split()))


# solution a
diff_0 = list(list_a.difference(list_b).union(list_b.difference(list_a)))
diff_0.sort() 
print("\n".join(map(str, diff_0)))

# listen 2 有说, a = sorted(a) 等同于 a.sort()




# solution b
# diff = list(list_a.union(list_b) - list_a.intersection(list_b))
# diff.sort() 
# print("\n".join(map(str, diff)))



------------------------------------------
这里的sss.add()和那个xxxx.sort() 一样，没有return值，直接对原始数据操作，a改变了
b = sorted(a)有return值，a不变
------------------------------------------
# 为啥需要srt（）
# join() expected str

# >>> "=".join([1,2,3])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: sequence item 0: expected str instance, int found

# >>> "=".join(["1","2","3"])
# '1=2=3'

------------------------------------------
# map(str, diff_0)是一个map() method，好比 sorted()
# int()是int method，两者输入的parameter参数是不一样的。
# 规定map需要（target_type，source）
# int() 需要 int（source）
# 但是！int（）只能对一个element改变，不能变list所以需要map（int，xxx）

# 前者是参数，后者是method
# confusing，but python就这些50个常用特性，之后慢慢用用就会了


------------------------------------------
>>> bin(10)
'0b1010'
>>> int(10)
10
>>> float(10)
10.0
>>> oct(10)
'0o12'
>>> hex(19)
'0x13'


>>> str(19)
'19'
>>> bin(1900)[0:3]
'0b1'
>>> hex(1900)[1:6]
'x76c'

结合今天的

------------------------------------------



------------------------------------------









