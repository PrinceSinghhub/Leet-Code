class Solution:
    def findLonely(self, nums):

        ans = []
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1

        print(d)

        for ele in d:
            if d[ele] == 1 and ele + 1 not in d and ele - 1 not in d:
                ans.append(ele)
        return ans

#         ans = []

#         for i in nums:
#             if nums.count(i) == 1 and i-1 not in nums and i+1 not in nums:
#                 ans.append(i)

#         return ans


ans = Solution()
nums = [10,6,5,8]
print(ans.findLonely(nums))