class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]

        numsExcludeLast = nums[:len(nums) - 1]
        numsExcludeFirst = nums[1:]

        excludeLastAns = self.robDP(numsExcludeLast)
        excludeFirstAns = self.robDP(numsExcludeFirst)

        return max(excludeLastAns, excludeFirstAns)

    def robDP(self, nums):
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return max(dp)

ans = Solution()
nums = [2,3,2]
print(ans.robDP(nums))
