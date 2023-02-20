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

        return start  # also return end point becouse start and end are at same point


r = Solution()
arr = [1,2,3,1]
print(r.findPeakElement(arr))