# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
set_country = set()
for i in range(n):
    country_name = str(input())
    set_country.add(country_name)
print(len(set_country))
