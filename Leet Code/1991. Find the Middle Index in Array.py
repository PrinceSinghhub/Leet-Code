class Solution:
    def findMiddleIndex(self, nums):
        leftSum = 0
        rightSum = sum(nums)

        for i in range(len(nums)):
            if leftSum == rightSum - nums[i]:
                return i

            leftSum += nums[i]
            rightSum -= nums[i]

        return -1

ans = Solution()
nums = [2,3,-1,8,4]
print(ans.findMiddleIndex(nums))