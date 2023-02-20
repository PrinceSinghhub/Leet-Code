class Solution:
    def longestCommonSubsequence(self, text1, text2):

        n1 = len(text1)
        n2 = len(text2)

        dp = [[0 for i in range(n2 + 1)] for j in range(n1 + 1)]
        for i in range(n1):
            for j in range(n2):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n1 - 1][n2 - 1]

ans = Solution()
text1 = "abcde"
text2 = "ace"
print(ans.longestCommonSubsequence(text1,text2))
a ="kfks"
print(sorted(a))