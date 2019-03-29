```
list comphrehension
L = [1,2,3,4]
L_plus = []
for i in L:
  L_plus.append[i+1]
  
print(L_plus)
  >>>[2,3,4,5,6]
---------------------------- 
  
L_plus2 = [i+2 for i in L]

print(L_plus)
  >>>[3,4,5,6,7]

---------------------------- 
ok= [1,6,7,3,8,4,2,9,5]
p = ok[-1] # p == 5
l = [x for x in ok[0:-1] if x <= p] + [p] + [x for x in ok[::-1] if x > p]

now 5 is in the middle of the list
ok= [1,3,4,2,5,6,7,9,8]

```

for jupyter notebook only     
!ls -g      
 list all of the files under current directory
 
