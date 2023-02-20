class Solution(object):
    def arrayPairSum(self, arr):
        arr.sort()
        ans = 0
        for i in range(0, len(arr) - 2 + 1, 2):
            ans += arr[i]
        return ans


ans  = Solution()
nums = [1,4,3,2]
print(ans.arrayPairSum(nums))


