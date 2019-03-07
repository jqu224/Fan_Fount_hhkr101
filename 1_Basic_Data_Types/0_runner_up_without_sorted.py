if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # solution a
    sorted_num = sorted(arr)
    for i in sorted_num[::-1]:
        if i < sorted_num[-1]:
            print(i)
            break

    # # solution b
    # # try 
    # # max_max, max_sec = 0, 0
    # max_max, max_sec = float("-inf"), float("-inf")
    # for i in arr:
    #     if i <= max_sec:
    #         pass
    #     elif i < max_max and i > max_sec:
    #         max_sec = i
    #     elif i > max_max:
    #         max_sec = max_max
    #         max_max = i
    # print(max_sec)
