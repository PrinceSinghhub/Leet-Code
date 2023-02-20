class Solution:
    def kthSmallest(self, matrix,k):
        ans = []

        for i in matrix:
            ans.extend(i)

        ans.sort()

        return ans[k - 1]

ans = Solution()
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(ans.kthSmallest(matrix,k))

