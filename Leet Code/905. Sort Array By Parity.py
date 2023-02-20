class Solution:
    def sortArrayByParity(self, nums):

        even = []
        old = []

        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                old.append(i)

        even.extend(old)
        return even

ans = Solution()
nums = [3,1,2,4]
print(ans.sortArrayByParity(nums))