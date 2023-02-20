class Solution:
    def targetIndices(self, nums, target):

        nums.sort()
        ans = []
        for i in range(len(nums)):
            if target == nums[i]:
                ans.append(i)
        return ans

ans = Solution()
nums = [1,2,6,5,8,7,4,1,3,9,7,4,5]
t = 4
print(ans.targetIndices(nums,t))