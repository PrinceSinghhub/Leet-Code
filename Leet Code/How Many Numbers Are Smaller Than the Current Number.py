class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # todo myapproch
        # res = []
        # for i in nums:
        #     c= 0
        #     for j in nums:
        #         if i>j:
        #             c+=1
        #     res.append(c)
        # return res
        # todo optimize code
        arr = sorted(nums)
        res = [arr.index(i) for i in nums]
        return res
nums = [8,1,2,2,3]
r = Solution()
print(r.smallerNumbersThanCurrent(nums))
