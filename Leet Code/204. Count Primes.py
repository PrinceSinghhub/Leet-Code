class Solution:

    def countPrimes(self, n):
        if n <= 2:
            return 0
        dp = [True] * n
        dp[0] = dp[1] = False
        for i in range(2, n):
            if dp[i]:
                for j in range(i * i, n, i):
                    dp[j] = False
        return sum(dp)

#     def isprime(self,num):

#         count = 2

#         while (count * count ) <= num:
#             if num%count == 0:
#                 return False

#             count +=1

#         return True


#     def countPrimes(self, n):


#         if n < 2:
#             return 0

#         arr = []
#         for i in range(2,n+1):

#             ans = self.isprime(i)
#             if ans == True and i < n:
#                 arr.append(i)

#         return len(arr)



ans = Solution()
n = 1259
print(ans.countPrimes(n))
