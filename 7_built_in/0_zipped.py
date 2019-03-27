https://www.hackerrank.com/challenges/zipped/problem


# # # # # # #
# solution b 
# Enter your code here. Read input from STDIN. Print output to STDOUT
 

student, tests = map(int, input().split())
int_list = []
for _ in range(tests):
    int_list += [list(map(float, input().split()))]

for a in zip(*int_list):
    print(sum(a) / tests)



# # # # # # 
# solution a
# Enter your code here. Read input from STDIN. Print output to STDOUT

student, tests = map(int, input().split())
int_list = []
for _ in range(tests):
    int_list += [list(map(float, input().split()))]

for a in zip(*[i for i in int_list]):
    print(sum(a) / tests)
