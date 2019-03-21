def average(array):
    # your code goes here
    temp = set(array)
    return(sum(temp)/len(temp))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
