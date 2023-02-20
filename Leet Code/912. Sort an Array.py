class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()

        return nums


ans = Solution()
nums = [5,2,3,1]
print(ans.sortArray(nums))
