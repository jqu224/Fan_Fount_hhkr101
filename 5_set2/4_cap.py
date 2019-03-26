https://www.hackerrank.com/challenges/py-the-captains-room/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

k = int(input())
int_str = list(map(int, input().split()) )

# time out error
# group_num = (len(int_str) - 1) / k
# for i in set(int_str):
#     if int_str.count(i) == 1:
#         print(i)

# solution a
full_rooms = sum(list(set(int_str))) * k
k_cap_minus1 = full_rooms - sum(int_str)
cap = k_cap_minus1 // (k - 1)
print(cap)


# solution b
# xiang bu chu b...int
