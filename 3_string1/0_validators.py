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
#  dont you ever make a silly mistake while typing the if statements
