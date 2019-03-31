⛵️： ????       
🐍： !!!       

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
 
a =animal(“fan”) 这是用“fan”这个参数，对a进行初始化 initialize，结果就是：建立一个anminal类型的实例 instance：a         

instance method是animal 这个class的 内部 defined function,          

such as eat() loud() in chinese         

为什么叫instance method呢
-------------------------------
因为我们只能使用 a+eat(): a.eat() 来传唤eat，         
也就是先叫出 实例名：instance a          
再叫 eat() 来召唤出 eat 里面的 code，          

不能通过             
类名+ eat()： chinese.eat() 来执行eat                    

这里的instance method是个全称
-----------------------------
一般analyst叫他method，或者defined function，         
只是对应static method 和 class method来说，他应该叫做 instance method，意思是 we call it （for eg, eat()）by its instance name         

如果可以用 chinese.eat() 来执行eat，那么这个eat就不是上面这么写了，         
那就叫class method，call it by its class name，因为是通过【类名】召唤他         


https://blog.csdn.net/weixin_35653315/article/details/78165645 
注意foo 和Foo区别，前者是后者的instace，后者是前者的class。         
你需要的就这些，当别人在说这些term的时候大概知道别人在说啥就行。不用深究，没完没了滴，又不是当码农，不用学这些。         


有一些放在class里但是在内部def外面, 这些变量，
譬如这个 blah         
他是被 aa = chinese()          

bb = chinese() 共享的，那么class method就用来操作 blah这些个共享的variables。         

static 是用来调用 class 外面的golbal variables的。。。那个更复杂了          



