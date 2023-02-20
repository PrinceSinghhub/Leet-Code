class Solution:
	def minDistance(self, word1, word2):
		"""
		word1 = "horse", word2 = "ros"

		lets solve the problem in DP approach
		"""
		m = len(word1) + 1
		n = len(word2) + 1

		dp = [[0]*n for _ in range(m)]

		for r in range(1,m):
			dp[r][0] = r

		for c in range(1,n):
			dp[0][c] = c

		for i in range(1,m):
				for j in range(1,n):
					if word1[i-1] == word2[j-1]:
						dp[i][j] = dp[i-1][j-1]
					else:
						dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
		return dp[-1][-1]

ans = Solution()
word1 = "horse"
word2 = "ros"
print(ans.minDistance(word1,word2))

