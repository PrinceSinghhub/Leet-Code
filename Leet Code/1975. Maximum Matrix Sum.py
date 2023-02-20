class Solution:
    def maxMatrixSum(self, matrix):

        s, c, z, m = 0, 0, 0, float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    c += 1
                if matrix[i][j] == 0:
                    z = 1
                s += abs(matrix[i][j])
                m = min(m, abs(matrix[i][j]))

        if c % 2 == 0 or z > 0:
            return s
        else:
            return s - m * 2


ans = Solution()

matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
print(ans.maxMatrixSum(matrix))
