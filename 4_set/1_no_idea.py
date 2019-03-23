# Enter your code here. Read input from STDIN. Print output to STDOUT
happiness = 0
n, m = map(int, input().split())
list_int = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))
# cant use list here, time limit exceeded error Terminated due to timeout :(

# folowing is the correct solution: 
# A = set(map(int, input().split()))
# B = set(map(int, input().split()))

for i in list_int:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)


>>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
set(['Hacker', 'Rank'])
这是字典，dict，
set（dict）returns unique keys

print(set(set(['H','a','c','k','e','r','r','a','n','k'])))
这个呢，两层set和一层set效果一样，


print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
这个是enumerate吧 list变成 （index, char）的tuple形势，set of tuple，
你发现两个r两个a都在，因为（1，r）和（2，r）这样是两个不同的element，
set() of these （1，r）和（2，r) tuples， gives u two tuples （1，r）和（2，r in the set
