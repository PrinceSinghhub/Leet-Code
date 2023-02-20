import math as m
class Solution:
    def jump(self, nums):
        Dp = [m.inf]*len(nums)

        Dp[0] = 0

        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                if i+j< len(nums):
                    Dp[i+j] = min(Dp[i+j],Dp[i]+1)
        print(Dp)
        return Dp[len(nums)-1]


ans = Solution()
nums = [2,3,1,1,4]
print(ans.jump(nums))