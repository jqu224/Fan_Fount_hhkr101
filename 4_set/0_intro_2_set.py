def average(array):
    # your code goes here
    temp = set(array)
    return(sum(temp)/len(temp))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

    
    
char是string的最小单位
“11”这个string 有两个char分别是“1”和“1”
“13”这个string 有两个char分别是“3”和“1”
“ab”这个string 有两个char分别是“a”和“b”
