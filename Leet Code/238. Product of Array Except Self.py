class Solution:
    def callfun(self,n,nums):

        ans = 1
        for i in range(len(nums)):

            if i == n:
                pass
            else:
                ans*=nums[i]
        return ans

    def productExceptSelf(self, nums):


        ans = []
        for i in range(len(nums)):
            element = self.callfun(i,nums)
            ans.append(element)
        return ans
ans = Solution()
nums = [1,2,3,4]
print(ans.productExceptSelf(nums))
