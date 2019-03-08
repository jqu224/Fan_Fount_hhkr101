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

# NOTES:
#     a[0:3] means a[0]and a[1] and a[2])
    
#     a[1:10:3] means select a[1] and a[4] and a[7], 
#       no a[10] no a[0] since a[0:10] stopped at a[9])


if __name__ == '__main__':
