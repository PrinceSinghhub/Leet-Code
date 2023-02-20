class Solution:
    def arrangeCoins(self, n):

        Stairs = 1
        while n > 0:
            if n >= Stairs:
                n -= Stairs
                if n == 0:
                    return Stairs
                Stairs += 1
            else:
                return Stairs - 1


ans = Solution()
print(ans.arrangeCoins(5))