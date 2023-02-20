class Solution:
    def rotate(self, nums,k):
        L = len(nums)
        k = k%L
        new_num = nums[L-k:] + nums[:L-k]
        # nums[:] = new_num for leet code
        return new_num


k=2
a=[-1,-100,3,99]
r = Solution()
print(r.rotate(a,k))

