class Solution:
    def findMaxConsecutiveOnes(self, nums):

        count = 0
        ans = []
        for i in nums:

            if i == 1:
                count += 1
            else:
                ans.append(count)
                count = 0
        ans.append(count)
        print(ans)
        return max(ans)


ans = Solution()
nums = [0,0,1,1,0,1]
print(ans.findMaxConsecutiveOnes(nums))