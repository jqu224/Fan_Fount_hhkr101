https://www.hackerrank.com/challenges/py-check-subset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
  
#   line 3+4 <=> line 7
# test_num = int(input()) 
# for _ in range(test_num):

for _ in range(int(input())):
    n1 = int(input())
    set_a = set(map(int, input().split()))

    n2 = int(input())
    set_b = set(map(int, input().split()))
 
    if set_a - set_b: # if a = {1,2} b ={2,3} then a-b == {1}: elements only appear in a
        print(False)
    else:
        print(True)

# solution b
for _ in range(int(input())):
    n1 = int(input())
    set_a = set(map(int, input().split()))

    n2 = int(input())
    set_b = set(map(int, input().split()))
 
    if len(set_a - set_b) == 0: 
        print(True)
    else:
        print(False)

