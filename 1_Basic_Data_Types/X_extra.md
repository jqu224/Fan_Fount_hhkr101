  
-----------------------------------------------------------------------------------
List:
https://www.w3schools.com/python/python_lists.asp
-----------------------------------------------------------------------------------
a = [] this is a list

### find the list of students with the 2nd lowest score:

what we want:

dict { 

  27:[quan fan], 

  28: [a b c], 

  100: [mememe]

}

return: [a b c] since 28 is the 2nd lowest score

-----------------------------------------------------------------------------------
u don t need that for loop, use i = sorted(sheet.keys())[1] to find the 2nd lowest score

----------------------------------------------------------------------------------- 
Q - 所以一开始 所有的score 都不在 sheet 里 所以就跑到 else， create 除了 一个list？ 这个list 都是名字？
-----------------------------------------------------------------------------------
A - use the 1st name as a start
-----------------------------------------------------------------------------------
  if a new 37: sheet[37] = ["quan"] that is creating a list using the first occurance
  and then: if a 37 in dict already sheet[37].append("fan") -> this gives use 37: ["quan", "fan"]
  



-----------------------------------------------------------------------------------

Q - 所以sheet[score]=[name]  这个score的意思是 score是key？然后name是value？
-----------------------------------------------------------------------------------
A - YEAH, list of names is the value here, 
-----------------------------------------------------------------------------------
    we have key:value as score:[name]
    
    NOTE: if you type: sheet[score] = name without the [] around the name, 
          you cant append that name like a list later on 
    
sheet.keys() -> gives you a list of all keys
sheet.values() gives u all of the values

-----------------------------------------------------------------------------------
>>> a={1:12}
{1: 12}

>>> a[1] = b
>>> a
{1: [2, 3, 4]}


following is addons  -   following is addons  -- following is addons  -   following is addons
-----------------------------------------------------------------------------------

for i in a[::-1]:
this is a for loop goes from the back

>>> a = "1234566"
>>> a
'1234566'
>>> a[::-1]
'6654321'

-----------------------------------------------------------------------------------

however, a[-1] last element


>>> a
'1234566'
>>> a[-1]
'6'
>>> a[-2]
'6'
>>> a[-4]
'4'
>>>


-----------------------------------------------------------------------------------

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!下周带电脑啊!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

-----------------------------------------------------------------------------------
Q - 但是不知道array里到底有几个数 所以索性直接用-1咯?
    那反过来 a[0]=1, a[1]=2?
-----------------------------------------------------------------------------------
A - right, a[-1] = a[ len(a) -1 ]
-----------------------------------------------------------------------------------

a = "123" 
len("123") == 3 
python starts from 0

a[0] = "1" 

a[1] == "2"
there is no a[3]
there is no a[len(3)]
-----------------------------------------------------------------------------------

>>> a
'1234566'
>>> len(a)
7
>>> a[len(a)]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

python will return error msg if you try to get a[ len(a) 

-----------------------------------------------------------------------------------

-----------------------------------------------------------------------------------
Q - “\n"是啥
-----------------------------------------------------------------------------------
A - new line char


>>> print("a")
a
>>> print("\na\n")

a

>>>

-----------------------------------------------------------------------------------

here, 
1. print("-".join(["1st line", "2nd line"])) 
    gives you "1st line-2nd line"

output:
>>> 1st line-2nd line

2. then, print("\n".join(["1st line", "2nd line"])) 
    gives you "1st line\n2nd line"

output:
>>> 1st line
>>> 2nd line

当你print一个string的时候，python检测到\n 的话就会自动换一行
 

-----------------------------------------------------------------------------------


dictName.keys() and dictName.values()


题目要求alphabitical，按首字母排列
so, we sorted( dictNmae.keys() )

-----------------------------------------------------------------------------------
Q - 所以这个sort不是sort数字了 sort 名字了 sort value了就是？
-----------------------------------------------------------------------------------

>>> sorted(["na","naa","nz","ns","an"])
['an', 'na', 'naa', 'ns', 'nz']

if 1st char is the same, compare the 2nd if ..2nd == 2nd compare 3rd char..... goes on and on ....


-----------------------------------------------------------------------------------

a, *b = list( map( int, input.split() ) )
input split这部分，read in input 是一个 list

>>> a, b = [1,2,3,4]
ValueError: too many values to unpack (expected 2)
>>> a, *b = [1,2,3,4]
>>> a
1
>>> b
[2, 3, 4]

name，*list 就把name=harsh list=["25" "26.5" …]

星号代表，无论后面有多少个，通通给我放进list


----------------------------------------------------------------------------------- 
Q - what does map mean 
-----------------------------------------------------------------------------------
A - 匹配… 命名…… 
-----------------------------------------------------------------------------------

    map(int, listName) 
        -> map everything inside listName as int
    line is a list of strings
    
before map to float: 
      a = ["12", "232", "32.1"]
after: 
      n = map(int, a)
        -> n == [12.0, 232.0, 32.1]

map is used here because:
  u cant float(a_list[])  u can only float("12.2") == 12.2
  
-----------------------------------------------------------------------------------
Q - 反正就是要这么写是么。。。
-----------------------------------------------------------------------------------
A - right, if you want to convert a list into float numbers
    list() convert a package into a list. 
-----------------------------------------------------------------------------------


>>> map(int, ["1","2","9"])
<map object at 0x000001D12F95E520>

>>> list(map(int, ["1","2","9"]))
[1, 2, 9]

虽然map了，但是还是object，等于list这个人包含多余身份信息，需要list（）把它打开，只拿出list的value部分


-----------------------------------------------------------------------------------

map 给 list string这些basic element套了很多外套……
- 一般看到这个 map，告诉自己这就是包装过的list
- 要脱去她的外包装，
- 就给她再套个list（）在外面，
- 她就真的变成list了

-----------------------------------------------------------------------------------
 # tuple is (a, b, ...) could be any length  
          # a = (1,3) is a tuple  
          # a = (1,3,5) is also a tuple  
          # just keep in mind tuple is immutable (cant modify whats inside)  
          # only list[] set() and dict{} are mutable, u can change the values  


Q - 所以 tuple 长的和list一样 但是不能改？
-----------------------------------------------------------------------------------
A - right!
-----------------------------------------------------------------------------------
avg = 0
if avg >10: 
  print("%.2f" % avg)
  
#### here avg = 12.3456

因为avg是个float浮点小数，print float要用%f，那么这个%.3f就是小数点后保留3位，譬如1.23456就是1.234了

-----------------------------------------------------------------------------------
avg初始化为0，
在code的时候，
有些var只在if出现过，
那么万一没有满足if condition，
就没有var这个数了，

最後return或者print的时候，
就会报错，
因为python会抱怨：这人说了个reference var我从没听过

Q - 哦 所以 如果没有满足if condition 就会print 0了吗 - 固定用法咯
-----------------------------------------------------------------------------------
A - 嗯，print 0也比程序报错好，报错会强制退出，initialize var这是好习惯
-----------------------------------------------------------------------------------

print("%.2f" % avg)
the 2nd % 代表，把后面的var map到前面的%f，等于代换进去string了


-----------------------------------------------------------------------------------
>>> print("haha you have %d a int and a %d int two" %(12, 30))
haha you have 12 a int and a 30 int two

Q - d means interger？
A - enen

Q - %.4 这里是typo吗
A - nope, that %.4f means decimal point hou mian 4 ge shuzi
    i give you a %.4f so you can ask me....this question
    let you know how to print and control the length of float   

string  --  string -- string  --  string -- string  --  string -- string  --  string -- string  --  string -- string  --  string -- 
-----------------------------------------------------------------------------------
>>> a = "this is a string"
>>> a
'this is a string'

>> a[-1] == "g" 

>> a[1] == "h"

a[1] means the 2nd char of string a

-----------------------------------------------------------------------------------

also, string cant be modified, so....

>>> a
'this is a string'
>>> a[1] = "c"
TypeError: 'str' object does not support item assignment

but this is doable:

>>> a = ["a","b","c"]
>>> a[1] = "z"
>>> a
['a', 'z', 'c']


-----------------------------------------------------------------------------------

>>> a = "this"
>>> a
'this'
>>> b = list(a)
>>> b
['t', 'h', 'i', 's']
>>> b[1] = "u"
>>> b
['t', 'u', 'i', 's']
>>> a = "".join(b)
>>> a
'tuis'

-----------------------------------------------------------------------------------
sum up of string  -- sum up of string -- sum up of string  -- sum up of string
-----------------------------------------------------------------------------------

if you are asked to replace one char in a string, do:
list(that string) as list of chars
modifiy the list
and then join the list, make it back to one piece

Q - 把string变成list就可以改里面的东西再join成string了？
A - dui 



set  --  set -- set  --  set -- set  --  set -- set  --  set -- set  --  set -- set  --  set -- 
-----------------------------------------------------------------------------------
Q - set[]是啥
-----------------------------------------------------------------------------------
A - set(a) return a list of unique numbers inside list_a....no need to know set() for now

set(["a", "z", "a", "c"]) = {"a", "z", "c"}

str char bool int float tuple都不能改


就only:
  set dict list 能改




