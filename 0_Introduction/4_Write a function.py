def is_leap(year):
    leap = False
    
    # Write your logic here
    #     pass means giving it a skip, 
    #     find the end of the if statment, 
    #     in this case, you skip and go staight to line 11
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        pass
    elif year % 4 == 0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))
