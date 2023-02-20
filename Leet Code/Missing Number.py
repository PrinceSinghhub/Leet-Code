# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums):

        i = 0
        while i<len(nums):
            correctIndex = nums[i]

            if(nums[i]<len(nums) and nums[i]!=nums[correctIndex]):
                self.swipeElement(nums,i,correctIndex)
            else:
                i+=1

        # find our element
        for index,value in enumerate(nums):
            if index!=value:
                return index

        return len(nums)

    def swipeElement(self,nums, i, correctIndex):
        tepm = nums[i]
        nums[i] = nums[correctIndex]
        nums[correctIndex] = tepm


ans  = Solution()
a = [9,6,4,2,3,5,7,0,1]
print(ans.missingNumber(a))