if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()) # again, a list of int value
    
    # integer_list = list(integer_list)
    
    t = tuple(integer_list) # convert the list of int into tuple()
    # tuple is (a, b, ...) could be any length
    # a = (1,3) is a tuple
    # a = (1,3,5) is also a tuple
    # just keep in mind tuple is immutable (cant modify whats inside)
    # only list[] set() and dict{} are mutable, u can change the values
    
    print(hash(t))
    
    # hash is hard core, no need to learn it now


# i dont know this one,
# sometimes you need to code by guessing, improvisations guys
