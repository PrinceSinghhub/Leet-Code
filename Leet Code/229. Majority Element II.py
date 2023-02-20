class Solution:
    def majorityElement(self, nums):

        myarr = list(set(nums))

        mid = len(nums) // 3

        ans = []

        for i in myarr:
            if nums.count(i) > mid:
                ans.append(i)

        return ans

ans = Solution()
nums = [3,2,3]
print(ans.majorityElement(nums))