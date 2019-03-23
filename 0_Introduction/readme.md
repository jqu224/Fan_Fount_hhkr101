the "easy" way：你进入每个file，
然后把光标放到filename前面擦掉文件夹名字，
然后写 desired_folder_name/original_file_name_unchanged.py然后点下文的commit


..................................
a = 10000
print(a)
print("a")
b = a
print(b)

程序发生了什么呢？

新建一个变量，名字叫做 a，让这个a 指向一个位置，这个位置上的数是 10000
pirnt（a）：
  user: python，请打印a这个变量，
  py:   好的，我找找，
        啊！a指向一个int数值，这个值等于10000
  py:   好的我打印出来了
