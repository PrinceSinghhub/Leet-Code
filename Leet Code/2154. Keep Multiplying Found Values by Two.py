class Solution:
    def findFinalValue(self, nums, original):

        if original not in nums:
            return original

        while original in nums:
            original = original * 2
        return original



ans = Solution()
nums = [5,3,6,1,12]
original = 3
print(ans.findFinalValue(nums,original))