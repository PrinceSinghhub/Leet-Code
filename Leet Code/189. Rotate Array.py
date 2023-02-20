class Solution:
    def rotate(self, nums,k):
        L = len(nums)
        k = k%L
        new_num = nums[L-k:] + nums[:L-k]
        nums[:] = new_num
        return nums

ans = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(ans.rotate(nums,k))