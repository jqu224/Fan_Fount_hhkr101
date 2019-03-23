# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input()) 
list_a = set(map(int, input().split()))

m = int(input())
list_b = set(map(int, input().split()))


# solution a
diff_0 = list(list_a.difference(list_b).union(list_b.difference(list_a)))
diff_0.sort() 
print("\n".join(map(str, diff_0)))

# solution b
# diff = list(list_a.union(list_b) - list_a.intersection(list_b))
# diff.sort() 
# print("\n".join(map(str, diff)))
