class Solution:
    def findPeakElement(self, nums):
        start = 0
        end = len(nums) - 1

        while start < end:

            mid = start + (end - start) // 2

            if (nums[mid] > nums[mid + 1]):
                end = mid

            if (nums[mid] < nums[mid + 1]):
                start = mid + 1

        return start

ans = Solution()
nums = [1,2,1,3,5,6,4]
print(ans.findPeakElement(nums))