class Solution:
    def maxProfit(self, prices):
        Min = float('inf')

        MaxProfit = 0

        for i in range(len(prices)):
            Min = min(Min, prices[i])
            MaxProfit = max(MaxProfit, prices[i] - Min)

        return MaxProfit


ans = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(ans.maxProfit(prices))