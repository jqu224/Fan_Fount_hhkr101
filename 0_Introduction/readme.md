the "easy" way：你进入每个file，
然后把光标放到filename前面擦掉文件夹名字，
然后写 desired_folder_name/original_file_name_unchanged.py然后点下文的commit


..................................
什么是指向：
========================
你有一个变量，就好象
书签

书签 a 夹在了第100页
```
每次你打开a的时候。你就到了第100页
第100页就是书签a指向的位置
第100页上有1块钱
1快钱就是位置上的值／

page_100 = "ahahaha"
a = page_100
print(a)
那么print（变量 a）就是按着a找到它指向的位置 page_100
这时候page_100写着 “ahahahaha”
那么print（a）
```
就是print
“ahahaha”
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

  
 ```
 x = int(input())
 在python内部发生了什么呢？
 
 建立一个变量x，使其指向int(input())的结果
 那么首先看最inner bracket，input()
 意思是take in 一个 string，
 （直到回车符号 “\n”出现，才算一个string）
 int(这个string)意思是：默认只有一个
 “123”\n
 这样的string，（“12 45”\n这样不行）
 然后把三个char字符组成的string： “123” 转换成 123 三位数字
把123 放入内存中，
然后让x指向这个123所在地位置。

print（x）就会
 ```

print：
123

 
 ```
 x = int(input())
 y = int(input())
 print（x,y）
 运行上面这三行
 
 程序会等待你输入两行：
 
 假设我输入的是：
 123 回车
 345 回车
 
 在python内部发生了什么呢？
 
 建立一个变量x，使其指向int(input())的结果 123
 建立一个变量y，使其指向int(input())的结果 345
 这样，python存了两个变量： x和y
 x和y指向的数值分别是：123和345
 
print（x，y）就会
 
 
 
 
 ```
print：
123 空1格 345
