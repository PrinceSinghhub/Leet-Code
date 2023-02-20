class Solution:
    def minimumDifference(self, nums, k):
        if len(nums) <= 1:
            return 0

        nums.sort()
        res = nums[k - 1] - nums[0]

        for i in range(k, len(nums)):
            res = min(res, nums[i] - nums[i - k + 1])

        return res



ans = Solution()
nums = [9,4,1,7]
k = 2
print(ans.minimumDifference(nums,k))