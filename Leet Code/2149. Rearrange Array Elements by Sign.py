class Solution:
    def rearrangeArray(self, nums):

        neg = []

        pos = []

        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)

        ans = []


        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])

        return ans

ans = Solution()
nums = [3,1,-2,-5,2,-4]
print(ans.rearrangeArray(nums))