# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums,val):

        while val in nums:
            nums.remove(val)
        return len(nums)


ans = Solution()
nums = [3,2,2,3]
val = 3
print(ans.removeElement(nums,val))


