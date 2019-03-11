def mutate_string(string, position, character):

    return string[:position] + character + string[position+1:]
    #  easy one, if you learned from the previous questions of strings
    
    def mutate_string(string, *position):
    # print(position[0], position[1])
    return string[:position[0]] + position[1] + string[position[0]+1:]
    
    #  easy one, if you learned from the previous questions of strings

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
     
