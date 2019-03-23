the "easy" way：你进入每个file，
然后把光标放到filename前面擦掉文件夹名字，
然后写 desired_folder_name/original_file_name_unchanged.py然后点下文的commit


..................................
========================
```
a = 10000
print(a)
print("a")
b = a
print(b)
```
程序发生了什么
```
新建一个变量，名字叫做 a，让这个a 指向一个位置，这个位置上的数是 10000
pirnt（a）：
  user: python，请打印a这个变量，
  py:   好的，我找找，
        啊！a指向一个int数值，这个值等于10000
  py:   好的我打印出来了
```

打印了：
 10000
 
```
print（“a”）：
  user: python，请打印“a”这个string，这个string里面只有一个char，
  py:   好的，我找找，
        啊！“a”就是一个char嘛
  py:   好的我打印出来了
```

打印了：
 “a”
 
 
 
```

b = a

print(b)
  user: python，请建立一个新变量名字b，让b等于a的值，打印b这个变量，，
  py:   好的，我找找，
        啊！a就是一个变量嘛，那么我让b等于a指向的值：10000也就是b = 10000
  py:   好的我要打印变量b了哦
        啊！b就是一个变量嘛，b指向的位置上面的值是 10000
```

打印了：
 10000

 
