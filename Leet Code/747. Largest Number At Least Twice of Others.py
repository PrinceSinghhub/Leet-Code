class Solution:

    def dominantIndex(self, nums):

        Max = max(nums)
        Mindex = nums.index(Max)

        nums.remove(Max)

        for i in nums:

            if i > Max // 2:
                return -1

        return Mindex

ans = Solution()
nums = [3,6,1,0]
print(ans.dominantIndex(nums))