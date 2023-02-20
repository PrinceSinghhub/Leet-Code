class Solution:
    def majorityElement(self, nums):

        Half = len(nums) // 2

        myarr = list(set(nums))

        for i in myarr:

            if nums.count(i) > Half:
                return i

#         brute force approch
#         Half = len(nums)//2

#         for i in nums:
#             if nums.count(i) > Half:
#                 return i


ans = Solution()
nums = [2,2,1,1,1,2,2]
print(ans.majorityElement(nums))