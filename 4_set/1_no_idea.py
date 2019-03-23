# Enter your code here. Read input from STDIN. Print output to STDOUT
happiness = 0
n, m = map(int, input().split())
list_int = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))
# cant use list here, time limit exceeded error Terminated due to timeout :(
这里不能用list是因为会报错，Compiler Message
Terminated due to timeout意思是：list太龙长了，处理不完了。

相反地，如果用set，就去掉了重复项，节省了tons of time和计算力。
计算力，就好比程序只有64之手，只能做10×64这么多数字，电脑也有极限，
是cpu和你的program的好坏决定的，不同电脑也有速度区别


Sets are significantly faster than lists when you are searching for a particular entry . Moreover it removes multiple entries:

a={1,1,1,1,2,2,2,3,3,3} 
print (a)

Will give the output : {1, 2, 3} If list is used time required would be much more resulting in a termination due to a timeout
    
那就是set用的是特殊的存储方法，找if char in set(a)比 if char in list_a 快

# folowing is the correct solution: 
A = set(map(int, input().split()))
B = set(map(int, input().split()))
    
    
for i in list_int:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)

# >>> for i in "12345":
# ...     print(i)
# ...
# 1
# 2
# 3
# 4
# 5


# >>> for i in 12334:
# ...     print(i)
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not iterable



# >>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
# set(['Hacker', 'Rank'])
# 这是字典，dict，
# set（dict）returns unique keys

# print(set(set(['H','a','c','k','e','r','r','a','n','k'])))
# 这个呢，两层set和一层set效果一样，


# print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
# set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
# 这个是enumerate吧 list变成 （index, char）的tuple形势，set of tuple，
# 你发现两个r两个a都在，因为（1，r）和（2，r）这样是两个不同的element，
# set() of these （1，r）和（2，r) tuples， gives u two tuples （1，r）和（2，r in the set


# set是无序的

# >>> set([1,2,3]) == set([3,1,2])
# True
# set 只关心element唯一性，不关心顺序

# 只是有时，题目给你的是标准输入，
# 你必须take in and deal with it。如果不input()处理掉，会影响arr = input()这行




