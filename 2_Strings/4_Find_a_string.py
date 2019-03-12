def count_substring(string, sub_string):
    len1 = len(string)
    len2 = len(sub_string)
    # ex: string == "1234567",  means len1 == 7
    #     sub_string == "234"   means len2 == 3
    ans = 0
    for i in range(0,len1-len2+1): # think about this one for a min
        # string[0:len2+0] = string[0:3] 
        #                       = "123" from index 0 to index 2 (len2 - 1 == 3, 
        # no match then i + 1
        # string[1:3]  = "234" from index 1 to index 3  
        
        if string[i:len2+i] == sub_string:
            ans += 1 # a+=1 -> a = a + 1
    return ans


if __name__ == '__main__':
    
    
# NOTES: # NOTES: # NOTES: # NOTES: # NOTES: # NOTES: # NOTES: # NOTES: 
#     a[0:3] means a[0]and a[1] and a[2])
    
#     a[1:10:3] means select a[1] and a[4] and a[7], 
#       no a[10] no a[0] since a[0:10] stopped at a[9])


the idea is: 
    string == "abcdefg" and 
    substring: "cde" with len() of 3
for i == 0: here string[0:3] -> [abc]defg != substring [] -> [cde]
for i == 1 we have string[1:4] -> a[bcd]efg != substring [] -> [cde]
for i == 2 we have string[2:5] -> ab[cdef]g == substring [] -> [cde] found!!! ans +1

and keep going until we reach the end of string1    



# NOTES: # NOTES: # NOTES: # NOTES: # NOTES: # NOTES: # NOTES: 
但是由于python 从0数到2， 0 1 2 是三个，正好 s[ 0 : len(s) ]就是== s

s = "abc"
s[ 0 : len(s) ] == s == s[0:3]

也就有了下文的：        
f 如果 string [ i: len2+i ] == sub_string 
这两个string 每个字符char全一样，那么就把计数器ans的值加上1

这里的前提得是，
需要满足 string [ i: len2+i ] == sub_string  
两个2string长度一致，才可以比较是不是一模一样
otherwise a!=b 


Q - 可不可以不用定义len(1) len(2) 直接都用len(string) 和 len(sub_string)呢」
—————————
thats ok, then your code could become harder for us to read, right?
