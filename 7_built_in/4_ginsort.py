https://www.hackerrank.com/challenges/ginorts/problem
    
    
# Enter your code here. Read input from STDIN. Print output to STDOUT

# solution a
string = input()
low = ""
upp = ""
odd = ""
eve = ""
for i in string:
    if i.islower():
        low += i
    elif i.isupper():
        upp += i
    elif int(i) % 2 == 1:
        odd += i
    elif int(i) % 2 == 0:
        eve += i
low = sorted(list(low))
upp = sorted(list(upp))
odd = sorted(list(odd))
eve = sorted(list(eve))
print("".join([*low,*upp,*odd,*eve]))


# solution b
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')
