class Solution:
    def isMonotonic(self, nums):
        check = nums.copy()

        check.sort()

        if nums == check or nums == check[::-1]:
            return True
        return False

#         Max = max(nums)

#         if nums.index(Max) == 0 or nums.index(Max) == len(nums)-1:
#             return True

#         return False

ans = Solution()
arr = [1,2,3,4,5,6,7,8,9,0,100]
print(ans.isMonotonic(arr))