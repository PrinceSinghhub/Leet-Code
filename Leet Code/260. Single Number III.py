class Solution:
    def singleNumber(self, nums):

        ans = []
        for i in nums:
            if nums.count(i) == 2:
                pass
            else:
                ans.append(i)
        return ans

ans = Solution()
nums = [1,2,1,3,2,5]
print(ans.singleNumber(nums))