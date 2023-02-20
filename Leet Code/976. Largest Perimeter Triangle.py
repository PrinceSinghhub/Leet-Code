class Solution:
    def largestPerimeter(self, nums):

        nums.sort()
        for x in range(len(nums) - 1, 1, -1):
            if (nums[x - 1] + nums[x - 2] > nums[x]):
                return (nums[x - 1] + nums[x - 2] + nums[x])
        return 0


ans = Solution()
nums = [2,1,2]
print(ans.largestPerimeter(nums))