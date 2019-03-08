def swap_case(s):

    # initialize a list of 0s 
    # len(0s) == len(s)
    list_a = [0]*len(s)
    
    # enumerate(a_list) is taking out elements from a_list, give (one at a time)
    # each time, generate a tuple (index_number, value)
    # for ex: s = "abcd" 
    #     then enumerate(s) gives us (0, "a"), (1, "b"), (2, "c")
    for i, c in enumerate(s):
        if c >= "a" and c <= "z":
            list_a[i] = s[i].upper()
        elif c>="A" and c <= "Z":
            list_a[i] = s[i].lower()
        else:
            list_a[i] = s[i]
    return "".join(list_a)

if __name__ == '__main__':
