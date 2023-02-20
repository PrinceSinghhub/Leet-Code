class Solution:
    def runningSum(self, nums):
        num = []
        Sum = 0

        for i in nums:
            Sum += i
            num.append(Sum)

            # num.append(sum(nums[0:i+1]))

        return num

ans = Solution()
nums = [1,2,3,4]
print(ans.runningSum(nums))
