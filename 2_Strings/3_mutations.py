def mutate_string(string, position, character):

    return string[:position] + character + string[position+1:]
    #  easy one, if you learned from the previous questions of strings
    


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c) # 注意，位置是一一对应的： string->s /// position-> int(i) /// character -> c
    print(s_new)
     
        
        
#     or    #     or    #     or    #     or    #     or    #     or
def mutate_string(string, *position): 
    # 这里position成了一个list，
    # 第一个element 是个int，5  
    # 第二个element 是char “k” 
    # position[0] is 5 position[1] is "k"
    return string[:position[0]] + position[1] + string[position[0]+1:]

    
#         #         #         #         #         #         #         #         #         #         #      
恩，2 diff points。
1，极端情况下需要星号 
    所以我写成了 return string[:position[0]] + position[1] + string[position[0]+1:] 

    那么这相当于，string, *position = s, int(i), c 所以：string = c 而 position = 【int(i)   c】
    提这是trick因为有时候不知道传入 defined function 的 argument 的长度

    就和 a, *b = list( [1 2 3 4 5 6] )一样呀，a == 1, b == [2 3 4 5 6]

2，list 可以由不同的type组成 

    譬如 int char string float 也可以list里套着别的【list【】】 

    例如：>>> a= [1, "a", 1.1, [1, 3], (3,4,5)]
    >>> a
    [1, 'a', 1.1, [1, 3], (3, 4, 5)]
    >>>


    用*号,就把 int(i) 给了position【0】，把 c 赋予了 position【1】，所以上面的 code 也是能 pass the tests 的
    s_new = mutate_string(“abracadabra ”,  5,  “k”)对吗？
    def mutate_string(string, *position): 
        这里，string == “abracadabra ” 
        而 position == [5,  “k”] 了
    >>> a[3]
            [1, 3]
    >>> a[4]
            (3, 4, 5)
    >>>

