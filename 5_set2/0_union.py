https://www.hackerrank.com/challenges/py-set-union/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
list_a = set(map(int, input().split()))

m = int(input())
list_b = set(map(int, input().split()))

print(len(list_a.union(list_b)))
