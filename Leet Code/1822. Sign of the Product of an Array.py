class Solution:
    def arraySign(self, nums):

        prod = 1
        for i in nums:
            prod *= i

        if prod > 0:
            return 1

        if prod < 0:
            return -1
        return 0

ans = Solution()

nums = [-1,-2,-3,-4,3,2,1]
print(ans.arraySign(nums))
