class Solution:
    def numIdenticalPairs(self, nums):
        res = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    res+=1
        return res

r = Solution()
n = [1,2,3]
print(r.numIdenticalPairs(n))
