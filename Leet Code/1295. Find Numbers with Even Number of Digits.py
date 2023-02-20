import math


class Solution:
    def findNumbers(self, nums):

        count = 0
        for i in nums:
            check = str(i)
            if len(check) % 2 == 0:
                count += 1

        return count

ans = Solution()
nums = [555,901,482,1771]
print(ans.findNumbers(nums))