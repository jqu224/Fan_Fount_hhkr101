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
