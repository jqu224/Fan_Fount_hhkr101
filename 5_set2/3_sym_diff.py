https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
e_set = set(map(int, input().split()))
m = int(input())
f_set = set(map(int, input().split()))
print(len(e_set.symmetric_difference(f_set)))
