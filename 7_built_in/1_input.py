https://www.hackerrank.com/challenges/input/problem
    
    
    
# Enter your code here. Read input from STDIN. Print output to STDOUT
x, ans = map(int, input().split())
poly = input()

if eval(poly) == ans:
    print(True)
else:
    print(False)

# Enter your code here. Read input from STDIN. Print output to STDOUT
x, ans = map(int, input().split()) 

if eval(input()) == ans:
    print(True)
else:
    print(False)

# Enter your code here. Read input from STDIN. Print output to STDOUT
x, ans = map(int, input().split()) 
print(True if eval(input()) == ans else False)
 
