def print_rangoli(size):
    # your code goes here
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    len_0 = size - 1
    lines = [(alpha[len_0:(len_0-i-1):-1] + alpha[size-i:size]) for i in range(len_0)]
    lines = ["-".join(i).center(size*4-3, "-") for i in lines] 
    
    print("\n".join(lines + ["-".join(alpha[size-1:0:-1] + alpha[:size])] + lines[::-1]))




if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

-----------------
    
Sample Input

5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

