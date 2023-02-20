class Solution:
    def pivotIndex(self, nums):

        ls = 0
        rs = sum(nums)

        for i in range(len(nums)):

            ls += nums[i]
            rs -= nums[i]

            if ls - nums[i] == rs:
                return i

        return -1

ans = Solution()
nums = [1,7,3,6,5,6]
print(ans.pivotIndex(nums))