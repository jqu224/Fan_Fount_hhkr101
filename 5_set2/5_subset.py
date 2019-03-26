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
        
        
----------------------------------------
>>> a
set()
>>> b
{65, 3, 54}
>>> a-b
set()
这里a-b为空 if a-b:此时这个if语句被认定为false，不执行if的内容

>>> a = {8,3}
>>> b
{65, 3, 54}
>>> a-b
{8}
这里不为空，此时if a-b 语句不等于空，if成立，True，return of a-b == True。执行if内容
