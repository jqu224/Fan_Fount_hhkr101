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
        for i in range(k):
            temp_list = list(string[i*k:i*k+k])
            temp_set = ""
            for x in temp_list:
                if x not in temp_set:
                    temp_set += x
            print(temp_set)

    # print("\n".join(ult_list))




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
