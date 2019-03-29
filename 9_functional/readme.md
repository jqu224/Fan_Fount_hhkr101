⛵️： ????     
🐍： !!!



。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
🐍：lambda is not important to analyst,     
   just go through my solution and call yourself happy     
   
   事实上，python对你也没有用。
   真正有用的是，numpy和pandas sql
   
   学python是为了下周用 pandas 和 numpy 操作 excel 表格
   
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
 ⛵️： 
 >> l = list(range(10))     
 >> l = list(map(lambda x:x*x, l))????     
🐍： !!！
   lambda x: x*x 意思是：for every x in the list，make x = x^2     
   
but, here we have 无名 function lambda     
lambda 和 for 不一样，for 需要 list 实例    
which allow us to （骗自己说）将来会有一个list，    
每个x都变成square of x了（画大饼你懂伐）    
   
   
   
   
   
   
   
   
   
   
   
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
   
⛵️： try后面的东西也看不懂？????     
🐍： !!!
try的意思是，lets try and okay to fail，譬如following code，z没有定义，本来print z会报错，但是try了以后。如果出错了，就让py跑except内的code：
    
```
>>> z   
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>   
NameError: name 'z' is not defined   
>>>    
>>>   
>>> try:   
...     print(z)   
... except:   
...     print(123)    
...   
123     
>>>    
>>> a
"aaaaaa"
>>> try:
...     print(a)
... except:
...     print(321)
...
“aaaaa”
```


。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
```
   try:
        username, url = email.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
```
⛵️： ValueError????       
🐍： !!!    
ValueError 是一种固定的error 形式，        
看到这种就去google：python valueerror        
    
继续将try，我知道怎么用，但是不会去用它。。        
因为我这个 analyst 工作的 project 是为了解决boss的问题，    
我的code是给自己写的，为了做数据分析，不是给用户或者别人的，      
接触不到try这种为了工程hardcore program而设计语句。     

但是，得知道怎么google，如果碰到了可以临时goole一下。不至于freak out     





。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

⛵️： if username.replace("-", "").replace("_", "").isalnum() is False:????     
🐍： !!!     
先replace“－” using empty char “”    
then replace ‘_’ using “”    
last，check is all elements in the parsed string （alpha or digit）    

```
>>> "1231=-2s.fdd=".replace("=","")
'1231-2s.fdd'
>>> "1231=-2s.fdd=".replace("=","  ")
'1231  -2s.fdd  '
```

isalnum() 之前学过。。。    

xxx.isdigit() check是不是1233..9    

xxx.isalpha() check是不是 abcd..z     
xxxx.isalnum()应该是both。。。    

overall：把username这个string 从左传递至右，     
依次: 先除去－再除去_ 最后看是不是alnum： alpha or digit      


>>> "12sdfdf323".isalnum()    
True    
>>> "12sdf+df323".isalnum()    
False    

  
为的是第二个rules，only contain alpha num    
Valid email addresses must follow these rules:    
 - It must have the username@websitename.extension format type.       
 - The username can only contain letters, digits, dashes and underscores.    
 - The website name can only have letters and digits.    
 - The maximum length of the extension is     
。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

⛵️： ????     
🐍： !!!










⛵️： ????     
🐍： !!!










⛵️： ????     
🐍： !!!











⛵️： ????     
🐍： !!!











⛵️： ????     
🐍： !!!













⛵️： ????     
🐍： !!!












⛵️： ????     
🐍： !!!
