class Solution:
    def divisorGame(self, n):
        if n % 2 == 0:
            return True

        return False


ans = Solution()
n = 14
print(ans.divisorGame(n))