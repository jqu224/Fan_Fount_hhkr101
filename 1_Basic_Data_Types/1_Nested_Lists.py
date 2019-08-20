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
        
#     detailed breakdown    #     detailed breakdown    #     detailed breakdown    #     detailed breakdown    
    # input:
    # 5
    # Harry
    # 37.21
    # Berry
    # 37.21
    # Tina
    # 37.2
    # Akriti
    # 41
    # Harsh
    # 39
    
    # code starts below
    # first create an empty dictionary    
    sheet = {}
    # or
    sheet = dict()
    #  a dict is bunch of pairs of keys: values
    #   such as {"key": 12, 1: "value"}
    #   in this case, use score as key and name_list as value  
    
    for _ in range(int(input())):   # this input catch the 1st num: 5 for once
        name = input()              # Harry
        score = float(input())      # 37.21
        if score in sheet:          # dict can only find by key, so if 37.21 is a key in sheet{}
            sheet[score].append(name) # append [name] to the end of the list of sheet[score] 
        else:                       # so if 37.21 is not a key in sheet{}
            sheet[score] = [name]   # create a list by [name] and pair it with sheet[score]
            #             note: ["Harry"] means a list with only one element "Harry"
            #               here name "Harry" is not the same as [name] which is "Harry"             
            # also try: 
            # row[score] = name
            
    # now we have 
    #     sheet =  {37.21: ['Harry', 'Berry'], 
    #                 37.2: ['Tina'], 
    #                 41.0: ['Akriti'], 
    #                 39.0: ['Harsh']}
    
    
    sec_last = float("-inf")  
    if len(sheet) > 1:
        sec_last = sorted(sheet.keys())[1]

    if sec_last in sheet:
        # print the list of 2nd lowest values line by line        
        print("\n".join(sorted(sheet[sec_last]))) # see extra from 0_intro folder
    else:
        print("Error occured")
