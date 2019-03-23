class Solution:
    
#         solution a
    def maximumSwap(self, num: int) -> int:
        a = list(str(num))
        rev_a = list(str(num))[::-1]
        sort_a = sorted(a)[::-1]
        for i, char in enumerate(a):
            if a[i] != sort_a[i]: 
                temp = a[i]
                a[i] = sort_a[i] 
                a[-rev_a.index(sort_a[i]) - 1] = temp 
                return int("".join(a)) 
        return num
                
        
#         solution b
#     def maximumSwap(self, num):
#     A = list(str(num))
#     ans = A[:]
#     for i in range(len(A)):
#         for j in range(i+1, len(A)):
#             A[i], A[j] = A[j], A[i]
#             if A > ans: ans = A[:]
#             A[i], A[j] = A[j], A[i]

#     return int("".join(ans))
