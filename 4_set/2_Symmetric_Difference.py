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

# listen 2 有说, a = sorted(a) 等同于 a.sort()




# solution b
# diff = list(list_a.union(list_b) - list_a.intersection(list_b))
# diff.sort() 
# print("\n".join(map(str, diff)))



# 为啥需要srt（）
# join() expected str

# >>> "=".join([1,2,3])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: sequence item 0: expected str instance, int found

# >>> "=".join(["1","2","3"])
# '1=2=3'
