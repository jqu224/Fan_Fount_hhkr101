这题，要求找到第二大的数值，2 3 5 5 6 6 return 5

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # solution a
    sorted_num = sorted(arr)
    for i in sorted_num[::-1]:
        if i < sorted_num[-1]:
            print(i)
            break
