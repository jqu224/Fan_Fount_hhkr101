import textwrap

def wrap(string, max_width):
    
#  solution a.1
    temp_list = list(string)
    # try for i in range(1, len(string)): and click run code
    for i in range(len(string)+1,1,-1):
        if i % max_width == 0:
            temp_list.insert(i, "\n")
    return "".join(temp_list)

#  solution a.2
    temp_list = list(string)
    # try for i in range(1, len(string)): and click run code
    for i in range(len(string)//max_width,0,-1): 
        temp_list.insert(i*max_width, "\n")
    return "".join(temp_list) 

#  solution b 
    answer = [] 
    for i in range(0,len(string),max_width): 
        answer.append(string[i:i+max_width])
    return "\n".join(answer)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    
=====   NOTES      =====   NOTES      =====   NOTES      =====   NOTES      =====   NOTES      =====   NOTES      
    
    insert(4, a)是吧a放在4，原来的4567位置上的瞬移到5678
    
for i =  4 8 12 在 abcdefghijk 的de中间和hi中间插入回车符号对不对？
要变成abcd [ ] efgh [ ] ijk :
第4个insert \n就成了：abcd[]efghijk 
第8个insert \n就成了：abcd【第一个回车】efgh【第2个回车】ijk 可是这时候 
【第一个回车】是第五个符号了，
所有符号index位置向后瞬移1位，现在在第八位后面insert的话就成了在ij中间了


this is why 要从后往前，
从后往前不会打乱前面的inde后面index被打乱没事，但是从前往后会打乱后面的inde，从后往前需要用。。。。

