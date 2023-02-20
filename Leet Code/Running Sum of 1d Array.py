class Solution:
    def runningSum(self, nums):
        ans = []
        for i in range(len(nums)):
            r=0
            for j in range(0, i + 1):
                r+=nums[j]
            ans.append(r)

        return ans
x=Solution()
n=[1,2,3,4,5]
print(x.runningSum(n))