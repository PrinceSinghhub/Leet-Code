class Solution:
    def maxProductDifference(self, nums):
        nums.sort()

        a, b = nums[-1], nums[-2]
        c, d = nums[0], nums[1]

        ans = (a * b) - (c * d)
        return ans

ans = Solution()
nums = [5,4,6,8,7,4,1,2,3,5,4,9,8,7,4,5,6,3,2,5,4,4,4,5,22,21]
print(ans.maxProductDifference(nums))

