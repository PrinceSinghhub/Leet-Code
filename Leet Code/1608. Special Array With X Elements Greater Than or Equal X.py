import bisect
class Solution:
    def specialArray(self, nums):
        nums.sort()
        for i in range(1, len(nums) + 1):
            startIndex = bisect.bisect_left(nums, i)
            if len(nums) - startIndex == i:
                return i
        return -1


ans = Solution()
arr = [1,2,3,4,5]
print(ans.specialArray(arr))