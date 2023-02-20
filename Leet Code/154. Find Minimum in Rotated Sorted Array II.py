class Solution:
    def findMin(self, nums):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            elif nums[low] < nums[mid]:
                high = mid - 1
            else:
                high -= 1
        return nums[low]

ans = Solution()
nums = [1, 3, 5]
print(ans.findMin(nums))