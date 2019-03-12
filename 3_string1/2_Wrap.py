import textwrap

def wrap(string, max_width):
    temp_list = list(string)
    # try for i in range(1, len(string)): and click run code
    for i in range(len(string)+1,1,-1):
        if i % max_width == 0:
            temp_list.insert(i, "\n")
    return "".join(temp_list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
