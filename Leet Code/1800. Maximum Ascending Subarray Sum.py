class Solution:
    def maxAscendingSum(self, nums):

        maxSum = nums[0]
        currentSum = nums[0]

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                currentSum += nums[i]

            else:
                currentSum = nums[i]

            if currentSum > maxSum:
                maxSum = currentSum

        return maxSum


ans = Solution()
arr = [10,20,30,5,10,50]
print(ans.maxAscendingSum(arr))