class Solution:
    def sortArrayByParityII(self, nums):

        even = []
        old = []

        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                old.append(i)

        ans = []
        for i in range(len(old)):
            ans.append(even[i])
            ans.append(old[i])

        return ans


ans = Solution()
nums = [1,3,4,5,8,7,16,12]
print(ans.sortArrayByParityII(nums))