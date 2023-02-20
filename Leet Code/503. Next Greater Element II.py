class Solution:
    def nextGreaterElements(self, nums):

        def nextgreater(num, arr):
            for i in arr:
                if i > num:
                    return i
            else:
                return -1

        ans = []
        for i in range(len(nums)):
            ans.append(nextgreater(nums[i], nums[i:] + nums[:i]))
        return ans

ans = Solution()
nums = [1,2,1]
print(ans.nextGreaterElements(nums))