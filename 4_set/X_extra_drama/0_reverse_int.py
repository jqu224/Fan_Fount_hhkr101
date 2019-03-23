class Solution:
    
            
# 1<<31 
# -> 1000000000000000000000000000 
# = 2147483648

# 1<<31 -1 
# -> 10000000000000000000000000000000 - 1 
# = 01111111111111111111111111111111

# >>> 1<<31 - 1
#     1073741824


    def reverse(self, x: int) -> int:
        
        temp = str(x)
        if temp[0] == "-":
            answer = int("-"+temp[:0:-1])
        else:
            answer = int(temp[::-1])
            
        if answer >= 1<<31 or answer < -1<<31:
            return 0
        else:
            return answer


#         answer = 0
#         if x == 0 or x > 2**31 -1 or x < -2**31:
#             pass 
#         else: 
#             sign = int(x/abs(x))
#             x *= sign
#             while x > 0:
#                 temp = x % 10
#                 answer *= 10
#                 answer += temp
#                 x = x // 10 
#             answer *= sign
            
#         if answer > 2**31 -1 or answer < -2**31:
#             return 0
#         else:
#             return answer
     
    
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
     
    
        
    
    
    
    
