if __name__ == '__main__':
    N = int(input())
    list_a = []
    for i in range(N):
        cmmd = input().split() 
        if cmmd[0] == "insert": 
            list_a.insert(int(cmmd[1]), int(cmmd[2])) 
        elif cmmd[0] == "remove":
            list_a.remove(int(cmmd[1]))
        elif cmmd[0] == "append":
            list_a.append(int(cmmd[1]))
        elif cmmd[0] == "sort":
            list_a.sort()
        elif cmmd[0] == "pop":
            list_a.pop()
        elif cmmd[0] == "reverse":
            list_a.reverse()
        elif cmmd[0] == "print":
            print(list_a)
            
# no detailed breakdown for this one,
#    take a look at this page: 
#    https://docs.python.org/3/tutorial/datastructures.html
            
# listname.insert(indexname, valuename)

# list.remove(x) Remove the first value = (x) from the list  

# list.append(x) Add an item to the end of the list.

# list.sort()    Sort the items of the list in place  

# list.pop(index) Remove the item at the given position in the list, and return it. 
#                 If no index is specified, a.pop() removes and returns the last item in the list.

# list.reverse() reverse: so [1 3 2 4] -> [4 2 3 1]
list是可以 [1,"a",[1,2]] ,
而array 特指same type elements
【3，2，4】or 【“a” "v" "w"】
