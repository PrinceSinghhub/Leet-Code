class Solution(object):
    def sortColors(self, nums):

        l = len(nums)
        for i in range(l):
            MeanValue = i
            for j in range(i,l):
                if nums[j] < nums[MeanValue]:
                    MeanValue = j

            temp = nums[i]
            nums[i] = nums[MeanValue]
            nums[MeanValue] = temp

        return nums

ans = Solution()
nums = [2,0,2,1,1,0]
print(ans.sortColors(nums))