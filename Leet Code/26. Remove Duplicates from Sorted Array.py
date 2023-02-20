class Solution:
    def removeDuplicates(self, nums):

        nums[:] = sorted(set(nums))
        return len(nums)


ans = Solution()
nums = [1, 1, 2]
print(ans.removeDuplicates(nums))