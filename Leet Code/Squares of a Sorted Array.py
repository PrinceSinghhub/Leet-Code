class Solution:
    def sortedSquares(self, nums):
        arr = nums
        result = []
        for i in arr:
            r = abs(pow(i, 2))
            result.append(r)
        result.sort()
        return result



r = Solution()
List = [-4,-1,0,3,10]
print(r.sortedSquares(List))