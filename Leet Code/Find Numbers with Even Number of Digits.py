# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/class Solution(object):
class Solution(object):
    def findNumbers(self, nums):

        res = 0
        for i in nums:
            i = len(str(i))
            if(i%2==0):
                res+=1

        return res
ans = Solution()
nums = [555,901,482,1771]
print(ans.findNumbers(nums))
