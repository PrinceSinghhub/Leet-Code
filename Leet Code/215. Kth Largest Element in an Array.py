class Solution:
    def findKthLargest(self, nums,k):
        nums.sort()

        return nums[-k]

ans = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(ans.findKthLargest(nums,k))


