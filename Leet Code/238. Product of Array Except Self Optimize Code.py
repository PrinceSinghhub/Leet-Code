class Solution:

    def productExceptSelf(self, nums):


        ans = []
        for i in range(len(nums)):
            ans.append(1)
        left = 1
        for i in range(len(nums)):
            ans[i] = ans[i]*left
            left = left*nums[i]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i]*right
            right = right*nums[i]
        return ans
ans = Solution()
nums = [1,2,3,4]
print(ans.productExceptSelf(nums))
