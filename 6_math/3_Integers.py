# Enter your code here. Read input from STDIN. Print output to STDOUT

# solution a
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a**b + c**d)

# solution b
a,b,c,d = (int(input()) for _ in range(4))
print (pow(a,b)+pow(c,d))
