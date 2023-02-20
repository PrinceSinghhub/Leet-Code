class Solution:
    def sortedSquares(self, nums):
        arr = nums
        result = []
        for i in arr:
            r = abs(pow(i, 2))
            result.append(r)
        result.sort()
        return result

ans = Solution()
arr = [-1,4,3,7,2]
print(ans.sortedSquares(arr))