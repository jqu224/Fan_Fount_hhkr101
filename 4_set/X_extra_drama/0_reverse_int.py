class Solution:

    原题：https://leetcode.com/problems/reverse-integer/
           
要求1 是把123翻转为321，如果是－1324这样，就要变成－4231
要求2 输入输出都不得超过正负2^31，

Q:这个 -2^31 到2^31-1的区间 是说reverse前还是后？
—————————
题目意思应该是都要吧，我只是偷懒，把answer check一下不要超过2^31, leetcode也让我过了


Q: 1<<31的单位是二进制，代表了十进制的2^31

line 22到31说的是
1<<31代表着：
二进制的1向左移动31位 
变成了
（这行还是二进制：）1000000000000000000000000000
 dec(1000000000000000000000000000 )等于十进制：2147483648
    
# 1<<31 
# -> 1000000000000000000000000000 
# = 2147483648

# 1<<31 -1 
# -> 10000000000000000000000000000000 - 1 
# = 01111111111111111111111111111111

# >>> 1<<31 - 1
#     1073741824


# solution a
    def reverse(self, x: int) -> int:
        
        temp = str(x)
        if temp[0] == "-":
            answer = int("-" + temp[:0:-1])
        else:
            answer = int(temp[::-1])
            
#             1<<31 means decimal value of binary(10^31)
        if answer >= 1<<31 or answer < -1<<31:
            return 0
        else:
            return answer
        
#         
if answer >=1<<31 
      return 0 
else
     return answer
确保了  return 的值 小于< 2^31



# solution b
#         answer = 0
#         if x == 0 or x > 2**31 -1 or x < -2**31:
#             pass 
#         else: 
#             sign = int(x/abs(x))
#   here we use sign to repersent + or -
#             x *= sign
#             while x > 0:
#                 temp = x % 10
#                 answer *= 10
#                 answer += temp
#                 x = x // 10 

这里定义了一个variable叫做sign == int(n / abs(n))也就是n除以n的绝对值，
这样sign就被用来存正负号了，value of sign = 1 or －1，
存好符号以后，调转123
while看作一个简洁版的for loop，条件为：只要while 这行的语句成立，一直loop

那么依次顺序为：x == 123
123 % 10 余3
把answer 0 乘以10 == 0
answer +=余数 => answer == 3
x等于x//10 => 
x ==12 while loop 继续

temp = 12%10 => temp ==2
answer 3 *10 == 30
answer+=temp => answer == 32
x//10 ==1 while loop 继续

x 1%10 => temp == 1
answer *10 => 320
320+1 => answer ==321
x //= 10就是0了
这时候while x>0不成立，这个loop就打破了。

这样123成了321

下文answer = answer*sign就把存着的x的正负号还给了answer  
#   here we use sign to restore the +- of x
#             answer *= sign
            
#         if answer > 2**31 -1 or answer < -2**31:
#             return 0
#         else:
#             return answer
     
    
# solution c
#         answer = 0
#         if x == 0 or x > 2**31 -1 or x < -2**31:
#             pass
#         elif x > 0: 
#             while x > 0:
#                 temp = x % 10 
#                 answer *= 10
#                 answer += temp
#                 x = x // 10  
#         elif x < 0: 
#             x *= -1 
#             while x > 0:
#                 temp = x % 10
#                 answer *= 10
#                 answer += temp
#                 x = x // 10 
#             answer *= -1
            
#         if answer > 2**31 -1 or answer < -2**31:
#             return 0
#         else:
#             return answer
     
    
        
    
    
    
    
