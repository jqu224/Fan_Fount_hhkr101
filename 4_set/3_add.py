# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
set_country = set()
for i in range(n):
    country_name = str(input())
    set_country.add(country_name)
print(len(set_country))


# >>> a = input()
# 这里python会让我一直输入，知道出现回车为止：234234   sdf9sd99923 99423 =-34= -=-=
# >>> a
# '234234   sdf9sd99923 99423 =-34= -=-= '


