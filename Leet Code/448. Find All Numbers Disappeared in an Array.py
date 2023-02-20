class Solution:
    def findDisappearedNumbers(self, nums):

        ans = []
        for n in nums:
            a = abs(n) - 1
            if nums[a] > 0: nums[a] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans

ans = Solution()
nums = [4,3,2,7,8,2,3,1]
print(ans.findDisappearedNumbers(nums))