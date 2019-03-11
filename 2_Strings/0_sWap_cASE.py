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
    
>>>> for c, value in enumerate(my_list, 4):
...     print(c, value)
...
4 apple
5 banana
6 grapes
7 pear   
    
    
    
    
