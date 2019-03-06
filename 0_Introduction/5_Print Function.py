if __name__ == '__main__':
    n = int(input())
    #####     star operator here 代表 unpack whats next
    #     sep表示接起来，如果这题用，sep="-"，就会变成1-2-3
    #     https://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean
    print(*range(1,n+1),sep='')
    #     "" means double quote with nothingg inside the "  ... "
    #     in python " and ' means the same thing, 
    #     but if you want print("how's goooogle?") >> how's google 
    #     you may want 'in the middle of "" or vice versa: print('wtf"s gooooogle!')
    
    #     however, a*2 = 2a a**2 = a^2 a**10 = a^10
