# print all of the people with second lowest score:
if __name__ == '__main__':
    # code starts below
    sheet = {}
    # or
    sheet = dict()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in sheet: 
            sheet[score].append(name)
        else:
            # pls try: 
            # row[score] = name
            sheet[score] = [name]
    sec_last = float("-inf")

    # score values: from max to min 
    for i in sorted(sheet.keys()):
    # or: sorted(list(sheet))
        # pls try:
        # if i < max(sheet.keys):
        if i > sorted(sheet.keys())[0]:
            sec_last = i
            break 

    if sec_last in sheet:
        print("\n".join(sorted(sheet[sec_last])))
    else:
        print("Error occured")
