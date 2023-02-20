class Solution:
    def permute(self,nums):
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        ans = []


        for i in range(len(nums)):
            m = nums[i]


            remLst = nums[:i] + nums[i + 1:]

            res = self.permute(remLst)
            for i in res:
                ans.append([m] + i)
        return ans
# another approch
class Solution:
    def helper(self, nums, temp, ans):
        if len(nums) == 0:
            ans.append(temp)
            return

        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i + 1:], temp + [nums[i]], ans)

    def permute(self, nums):
        ans = []
        self.helper(nums, [], ans)
        return ans

ans = Solution()

nums = [1,2,3]
print(ans.permute(nums))