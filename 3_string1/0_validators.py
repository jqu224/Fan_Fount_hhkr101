if __name__ == '__main__':

# print True if string S

# has any lowercase characters. Otherwise, print False. 
islower() 是 check 是否全为lower case 
cant be used directly 

>>> print("asdD3".islower())
False
>>> print("asd3".islower())
True
    
#     solution a
#     这 a 是我抄来的
for把 c in str 变成了list，
譬如 str == qA2：那么c.isupper() for c in str 会 return [false true false]，
接着外面的any()这个语法是：只要出现过 true more than once 就 return true

    str = input()
    print(any(c.isalnum()  for c in str))
    print(any(c.isalpha() for c in str))
    print(any(c.isdigit() for c in str))
    print(any(c.islower() for c in str))
    print(any(c.isupper() for c in str))
    
#     solution b
    
嫌弃这个太复杂就用solution b，我只会，逻辑简单写，
先定义4个anylower anyupper为false，
把str for loop一遍，有islower就把一个anylower的牌子翻过来变成true，最后return anylower anyupper
    s = input()
    # first define 5 var for the outcomes
    anyAlphanumeric  = 0
    anyAlphabetical  = False
    anyDig = 0
    anyLower = 0
    anyUpper = 0
    for i in range(len(s)):
        if s[i].isalnum() and anyAlphanumeric == 0:
            anyAlphanumeric = 1

        if s[i].isalpha() and anyAlphabetical == 0:
            anyAlphabetical = True

        if s[i].isdigit() and anyDig == 0:
            anyDig = 1

        if s[i].isupper() and anyUpper == 0:
            anyUpper = 1

        if s[i].islower() and anyLower == 0:
            anyLower = 1

    print(bool(anyAlphanumeric))
    print(anyAlphabetical)
    print(bool(anyDig))
    print(bool(anyLower))
    print(bool(anyUpper))

#  remember the most important thing is to do the lian-lian-look
#  dont you ever make a silly mistake while typing the if statements pls


上次的🌰，只是告诉你要小心，
很多时候，return的答案不对，
是因为code的时候，if case的<>=这些边界条件设计不对 

但是呢，有时候，这个if里面的操作很复杂，
就可以把这个anyvalue判断放在if后面用and连接，
这样就不必做重复操作了 像这样的话，最好还是让if多判断一下，
只有在这个char是alpha且没有翻过anyalphaetidcal牌子的情况下，
``` 
        if s[i].isdigit() and anyDig == 0:
            anyDig = 1
            anyDi1g = 1
            anyDig2 = 1
            anyDig3 = 1
            anyDi4g = 1
            anyDig6 = 1
```
我们才进去做这一长串的any = 1赋值 
这里的重复操作是anylower = 1，也就是对把anylower变成true，这里比较简单跑一次也不碍事，所以and后面的可以不写 换句话说： 这个if我进去玩过了，这次是我的第二次路过这个if isdigit == true，就不进去了


