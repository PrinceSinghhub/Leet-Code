class Solution:
    def thirdMax(self, nums):
        nums = list(set(nums))

        if len(nums) < 3:
            return max(nums)

        nums.sort()
        return nums[-3]

ans = Solution()
nums = [3,2,1]
print(ans.thirdMax(nums))