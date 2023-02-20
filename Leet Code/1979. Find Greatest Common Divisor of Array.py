class Solution:
    def findGCD(self, nums):

        Max=max(nums)
        Min = min(nums)

        MaxList = []
        MinList = []
        for i in range(1,Max+1):
            if Max%i==0:
                MaxList.append(i)
        for i in range(1,Min+1):
            if Min%i==0:
                MinList.append(i)

        ans = max(list(set(MaxList) & set(MinList)))
        return ans

ans = Solution()
nums = [3,3]
print(ans.findGCD(nums))

