class Solution:
    def createTargetArray(self, nums,index):
        res = []
        r = 0
        for i in index:
            res.insert(i,nums[r])
            r+=1
        return res

nums = [0,1,2,3,4]; index = [0,1,2,2,1]
r = Solution()
print(r.createTargetArray(nums,index))
