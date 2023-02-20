class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 1: return 0
        digits = len(str(n))

        dp = [0] * digits
        for i in range(1, len(dp)):
            dp[i] = 10 ** (i - 1) + 10 * dp[i - 1]

        ans = 0
        for i in range(digits):
            lead, n = divmod(n, 10 ** (digits - i - 1))

            if 2 > lead >= 1:
                ans += dp[digits - i - 1] + n + 1
            elif lead >= 2:
                ans += lead * dp[digits - i - 1] + 10 ** (digits - i - 1)

        return ans
# class Solution:
#     def countDigitOne(self, n: int) -> int:


#         # bruteforce Apprch
#         if n == 0:
#             return 0

#         if n > 0 and n < 10:
#             return 1

#         ans = 0
#         List = []
#         for i in range(n+1):

#             List.append(str(i))

#         for j in List:

#             ans+=j.count('1')

#         return ans






ans = Solution()
n = 13
print(ans.countDigitOne(n))