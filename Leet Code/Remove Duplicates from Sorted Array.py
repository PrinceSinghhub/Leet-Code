# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums):


        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if j < len(nums):
        #             if nums[i] == nums[j]:
        #                 nums.remove(nums[i])
        # print(nums)
        nums[:] = sorted(set(nums))
        return nums


ans = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(ans.removeDuplicates(nums))


