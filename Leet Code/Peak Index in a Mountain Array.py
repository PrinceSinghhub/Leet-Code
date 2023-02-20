class Solution:
    def peakIndexInMountainArray(self, arr):

        res = max(arr)
        return arr.index(res)

r = Solution()
arr = [24,69,100,99,79,78,67,36,26,19]
print(r.peakIndexInMountainArray(arr))