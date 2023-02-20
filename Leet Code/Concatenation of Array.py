class Solution:
    def getConcatenation(self, nums):
        res = nums
        res.extend(nums)
        print(res)

r = Solution()
n = [1,2,1]
r.getConcatenation(n)
