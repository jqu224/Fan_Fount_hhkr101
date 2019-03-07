# 这题，要求找到第二大的数值，2 3 5 5 6 6 return 5
# for starter 就写a，
# 面试会要求写成b，因为基本上面试不让用 sorted() 函数，所以 b 也要明白怎么写的
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # # solution b
    
    # # try 
    # # max_max, max_sec = 0, 0
    #   the same as
    #   max_max = 0
    #   max_sec = 0
    #   need to inticialize max1 and max2 to -infinity in case there are minus values
    max_max, max_sec = float("-inf"), float("-inf") # only use float("-inf") -> cant use int("-inf") to get minus infinity
    for i in arr:
        if i <= max_sec:
            pass
        elif i < max_max and i > max_sec:
            max_sec = i
        elif i > max_max:
            max_sec = max_max
            max_max = i
    print(max_sec)
    #   let us go through an instance:  
    #     [1 5 4 5 6 3] 
    #     we go from 1 -> 5 -> 4 ... 
    #     max1 is the largest 
    #     max2 is second to max1
    #     [1] 5 4 5 6 3 -> first set i to 1, max1 = -inf, max2 = -inf,   
    #           falling into condition (c)  i > max1 > max2
    #           so update max2 = max1                                     [now: max2: previous max1; max1: -inf]
    #           and then max1 = i                                         [now: max2: -inf; max1: 1]
    #     1 [5] 4 5 6 3 -> set i to 5 (this is the second last element)            ||
    #           falling into condition (c)  i > max1 > max2                        \/
    #          so update max2 = max1                                     [now: max2: 1; max1: 1]
    #            and then max1 = i                                       [now: max2: 1; max1: 5] 
    #     1 5 [4] 5 6 3 -> set i to 4                                                 |
    #          falling into condition (b)  max1 > i > max2                           \|/
    #          so max2 = i = 4 no need to update max1                    [now: max2: 4; max1: 5] 
    #     1 5 4 [5] 6 3 -> set i to 5,                                                   ||
    #           we have i == max1 -> update nothing                                     \||/
    #     1 5 4 5 [6] 3 -> set i to 6                                                    \/
    #           falling into condition (c)  i > max1 > max2  
    #           so update max2 = max1                                    [now: max2: 5; max1: 5]
    #            and then max1 = i                                       [now: max2: 5; max1: 6] 
    #     1 5 4 5 6 [3] -> set i to 3                                                    \/
    #           falling into condition (a)  i < max2 < max1
    #           no need to update max1  ->  let us call it a day:P

# NOTES: 
# we only keep the two largest [value]
# 这种有难度的题， 最好写一下 logic 草稿 
# 
# 1.0是浮点数，python就是float，有小数点的
# 10是整数 integer， python 里 叫 int 
# 
# in python int and float 可以混用，之后会说 
# 
# since we are tracking value not specific number
# when we have i == max1 or == max2 
#   means u dont need to update max1 nor max2
# 
# 我的方法就是
# 设 两个var，maxmax和maxsecond，
# 初始化为负无穷-inf，
#  if input  i 小于maxsec则不记录，
#  if        i 在secondmax和maxmax中间则更新secondmax为i， 
#  if        i 大于maxmax则把maxmax传递给maxsec然后用i换掉maxmax 
# 
# 注意次序和等于号的使用 
# 
# if后的判断式 如写 ＞=是不对的
#     为啥第三种if condition里，
# 需要用i update 第二大max2先 再update 最大的max1呢？
# 因为，这里i成了最大的，原先的max1需要传给max2，如果反过来就不行
