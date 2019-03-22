Sample Input
  AABCAAADA
  3   
Sample Output
  AB
  CA
  AD
  
AAB -> AB
CAA -> CA
ADA -> AD
==================================================
def merge_the_tools(string, k):
    # your code goes here 
    if k == 1:
        print("\n".join(list(string)))
    else:    
        # there will be len / k lines since n is always a multiple of k 
        for i in range(len(string)//k):
            # chop off [0:k] [k:2k] [2k:3k] ....
            temp_list = list(string[i*k:i*k+k])
            # create a temp string for unique char in [0:k] ... and so on 
            temp_set = ""
            # loop through the [0:k] lists
            for x in temp_list:
                # if current char is not in the temp string 
                # then append it to the end of temp string
                if x not in temp_set:
                    temp_set += x
            print(temp_set)
 




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
