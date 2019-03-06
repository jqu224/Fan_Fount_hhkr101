if __name__ == '__main__':
    n = int(input())
    #####     star operator here 代表 unpack whats next
    #     sep表示接起来，如果这题用，sep="-"，就会变成1-2-3
    #     https://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean
    print(*range(1,n+1),sep='')
    
    #     however, a*2 = 2a a**2 = a^2 a**10 = a^10
