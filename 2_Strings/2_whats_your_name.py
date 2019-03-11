def print_full_name(a, b):
    print("Hello %s %s! You just delved into python." %(a, b))

    # also concatenation:
    # print("Hello "+ a + " " + b +"! You just delved into python.")  # same output

    # intuitive, take a closer look at the syntax
    #  print("Hello %d %d! You just delved into python." %(a, b))  #  for int numbers aa and bb
    #  print("Hello %.3f %.4f! You just delved into python." %(a, b)) 
    #           #  for float numbers aaa and bbb with 3 or 4 decimal points

if __name__ == '__main__':
