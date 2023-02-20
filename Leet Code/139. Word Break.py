class Solution:
    def wordBreak(self, s, wordDict):

        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True

        print(dp)
        return dp[-1]

ans = Solution()
s = "leetcode"
wordDict = ["leet","code"]
print(ans.wordBreak(s,wordDict))