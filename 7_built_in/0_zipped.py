https://www.hackerrank.com/challenges/zipped/problem


# # # # # # #
# solution a
# Enter your code here. Read input from STDIN. Print output to STDOUT
 

student, tests = map(int, input().split())
int_list = []
for _ in range(tests):
    int_list += [list(map(float, input().split()))]
  
for a in zip(*int_list):
    print(sum(a) / tests)
  
  
# 星号是用来unpack的，譬如 
# int_list = [ [list_a], [list_b], [list_c] ]
# *int_list = [list_a] [list_b] [list_c]
# 这样才能传入：zip()，
# zip()是把()内的所有的list的 第一个map到一个tuple或者list里， tuple还是list由你选择
# 第 2 个map到一个tuple或者list里，
# 第 3 个map到一个tuple或者list里...
# 譬如 list(zip( [1, 11, 111], [2, 22, 222] [3, 33, 333] )) => [（1,2,3）, （11,22,33）,（111,222,333）]
# 又譬如 tuple(zip( [1, 11, 111], [2, 22, 222] [3, 33, 333] )) => （（1,2,3）,（11,22,33）,（111,222,333））



# # # # # # 
# solution a.2
# Enter your code here. Read input from STDIN. Print output to STDOUT

student, tests = map(int, input().split())
int_list = []
for _ in range(tests):
    int_list += [list(map(float, input().split()))]

for a in zip(*[i for i in int_list]):
    print(sum(a) / tests)
