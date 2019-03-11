def swap_case(s):

    # initialize a list of 0s 
    # len(0s) == len(s)
    list_a = [0]*len(s)
    
    # enumerate(a_list) is taking out elements from a_list, give (one at a time)
    # each time, generate a tuple (index_number, value)
    # for ex: s = "abcd" 
    #     then enumerate(s) gives us (0, "a"), (1, "b"), (2, "c")
    for i, c in enumerate(s):
        if c >= "a" and c <= "z":
            list_a[i] = s[i].upper()
        elif c>="A" and c <= "Z":
            list_a[i] = s[i].lower()
        else:
            list_a[i] = s[i]
    return "".join(list_a)




if __name__ == '__main__':

    
# 1 NOTE NOTE NOTE NOTE NOTE  # 1 NOTE NOTE NOTE NOTE NOTE  # 1 NOTE NOTE NOTE NOTE NOTE  # 1 NOTE NOTE NOTE NOTE NOTE

>>> for c, value in enumerate(my_list):
...     print(c, value)
...
0 apple
1 banana
2 grapes
3 pear   


如果是for i，c in enumerate(list，10)，那么i就是从10开始10 11 12 13

>>>> for c, value in enumerate(my_list, 4):
...     print(c, value)
...
4 apple
5 banana
6 grapes
7 pear   
    
# 1 NOTE NOTE NOTE NOTE NOTE  # 1 NOTE NOTE NOTE NOTE NOTE  # 1 NOTE NOTE NOTE NOTE NOTE  # 1 NOTE NOTE NOTE NOTE NOTE
    
to help other human beings to understand my code 
we used i for index number and c for list element 
for i, c in enumerate(list):  gives us (0, "a"), (1, "b"), (2, "c")
    
    
enumerate(s) gives us (0, "a"), (1, "b"), (2, "c")
for #0, s[0] == "a" :  
            set temp_list[0] to "A"
for #1, s[1] == "b" :  
            set temp_list[1] to "B"
for #2, s[2] == "W" :  
            set temp_list[1] to "w"
then we have: temp_list = ["A", "B", "w"] 
    
Q - 所以 for x,y in enumerate(list) python自动知道 x是序列号 y是value？
    每一个（i,c)都是一个tuple是么
A - right    
    
    
enumerate(s)，给了我们 [(0，"element0") (1，"element1")……] 这么一串tuple
enumerate(s, 7)，给了我们[(7，"element0") (8，"element1")…(9, element2)…]这么一串tuple

而for x，y in enumerate(s) loop的时候每次取出一对x，y而已 
here for loop 等于脱去 tuple 的括号，拿出第一个赋予x，拿出第二个给y
    
