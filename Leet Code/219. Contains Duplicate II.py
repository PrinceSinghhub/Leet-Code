class Solution:
    def containsNearbyDuplicate(self, nums, k):

        dic = {}
        for index, key in enumerate(nums):
            if key in dic and index - dic[key] <= k:
                return True
            dic[key] = index
        return False

ans = Solution()
nums = [1,2,3,1,2,3]
k = 2
print(ans.containsNearbyDuplicate(nums,k))
