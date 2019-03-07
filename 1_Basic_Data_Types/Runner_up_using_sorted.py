# 这题，要求找到第二大的数值，[2 3 5 5 6 6] return 5
# # solution a: idea
#     a = sorted(b) 
#         ----- if b = [1,3,2] then a is = [1,2,3]
#     for i in a[::-1]: 
#         ------ this means go through list a from the back----i.e. i = 3 ->2 ->1
#     if i < a[-1] 
#         ---> a[-1] is the last element in list a....in this case a[-1] = 3 

# if we have 
#   arr =  [1 2 3 4 5 6 7 98 9 ]
# list_a = sorted(arr) 
#       - > [1 2 3 6 7 9 98] we go from the back using [::-1]
#       - > first set i to 98, here i == a[-1] == 98skip
#       - > set i to 9 (this is the second last element)  
#           i < a[-1] ... found the second largest value!
#       - > return or print the value
#       - > break the loop. 
for i in sorted_num[::-1]:
    if i < sorted_num[-1]:
        print(i)
        break
        
        
        
        
        
        
            
            
#        following is the explanation    #        following is the explanation    #        following is the explanation
#        following is the explanation    #             explanation #             explanation #             explanation

#     井号就是comment out，python识别为人话，不给与执行
sorted_num = sorted(arr)    # easier for us to start from a = sorted(list) -> a[::-1] -> i = 98 ... 9 ... 7

#     also
a = sorted([98 3 45])       # a = [3 45 98]

# this a = sorted(b), 
#     a and b could be any char 
#  i named it that way... and yes and no, it is good to get it a meaningful name. 
#  especially when you are going to use it couple of times in your code...  
#  so that interviewer like your coding style. it is about getting hired
#       unlike for i, a , b these are counter values, which could be single char...

a = sorted(b)  #  means 
#     1st take the input(), which is string " 2 3 6 6 5 "
#       2nd split() it and get a list of char ["2" "3" "6" "6" "5"]
#           3rd and then map() it using int(), and get a list of int [ 2 3 6 6 5]

        
        
# if we have:
for i in range(10):
    for x in range(xx):
        if x == 10:
              break # ----here we only break the closest loop: 
                    #     i.e. [for x in range(xx)] and continue with the outer loop
            
# NOTE # NOTE # NOTE # NOTE # NOTE # NOTE # NOTE # NOTE # NOTE # NOTE # NOTE # NOTE # NOTE 
# # The syntax of sorted() method is: 
#       sorted(iterable[, key][, reverse]) 
# sorted() takes two three parameters: 
#       iterable - sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any iterator 
#       reverse (Optional) - If true, the sorted list is reversed (or sorted in Descending order)
#       key (Optional) - function that serves as a key for the sort comparison
# Return value from sorted()
#       sorted() method returns a sorted list from the given iterable.

