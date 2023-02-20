class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(result)

ans = Solution()
nums = [-1,0,1,2,-1,-4]
print(ans.threeSum(nums))
