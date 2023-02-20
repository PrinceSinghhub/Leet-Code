class Solution:
    def permuteUnique(self, nums):
        perms = [[]]
        for n in nums:
            perms = [p[:i] + [n] + p[i:]
                     for p in perms
                     for i in range((p + [n]).index(n) + 1)]
        return perms


ans = Solution()
nums = [1,2,3]
print(ans.permuteUnique(nums))