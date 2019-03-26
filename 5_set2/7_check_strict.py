https://www.hackerrank.com/challenges/py-check-strict-superset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

list_a = set(map(int, input().split()))

# b - a 为空，则b全在a中。true。 
# b - a 不为空，则b全在a中。false。
    # 只要有一个 b - a 是 false， overall 的 return/print 就是 false
# 用一个boolean value： temp 存 b - a
temp = 1
for _ in range(int(input())):
    list_b = set(map(int, input().split()))
    # 只要有一个 b - a 是 false，整个for loop就是false
    # 所以这里，false的情况有唯一性，只要抓住一次false，
    # 就让temp一直为false，整体有再多的true也不可改变 temp 的 
    if list_b - list_a:
        temp = 0 
        
        
print(bool(temp))
