https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
list_a = set(map(int, input().split()))

m = int(input())
list_b = set(map(int, input().split()))

print(len(list_a.intersection(list_b)))
