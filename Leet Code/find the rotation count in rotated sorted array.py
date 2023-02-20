# https://practice.geeksforgeeks.org/problems/rotation4723/1#
class Solution:
    def ans(self,nums):

        pivot = self.FindNumberofCoubt(nums)
        return pivot+1

    def FindNumberofCoubt(self,nums):
        start = 0
        end = len(nums) - 1

        while (start <= end):
            mid = start + (end - start) // 2

            # 4 cases over here
            if (mid < end and nums[mid] > nums[mid + 1]):
                return mid
            if (mid > start and nums[mid] < nums[mid - 1]):
                return mid - 1
            if (nums[start] >= nums[mid]):
                end = mid - 1
            if (nums[start] <= nums[mid]):
                start = mid + 1

        return -1


ans = Solution()
a = [7, 9, 11, 12, 5]
print(ans.ans(a))