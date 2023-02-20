class Solution:
    def numDecodings(self, s):
        if s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, len(s)):
            if s[i] != "0":
                dp[i + 1] = dp[i]
            else:
                dp[i + 1] = 0
            if s[i - 1] != "0" and int(s[i - 1] + s[i]) <= 26:
                dp[i + 1] += dp[i - 1]

        print(dp)
        return dp[-1]


ans = Solution()
s = "226"
print(ans.numDecodings(s))