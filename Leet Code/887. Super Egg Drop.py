class Solution:
    def superEggDrop(self, K, N):
        dp = [[0] * (K + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, K + 1):
                dp[i][j] = 1 + dp[i - 1][j - 1] + dp[i - 1][j]
            if dp[i][j] >= N:
                return i

ans = Solution()
print(ans.superEggDrop(1,2))