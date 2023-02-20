class Solution:
    def canBeIncreasing(self, nums):
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                count += 1
                if i>1 and nums[i] <= nums[i-2]:
                    nums[i] = nums[i-1]
        return count <= 1

ans = Solution()
nums = [1,2,10,5,7]
print(ans.canBeIncreasing(nums))