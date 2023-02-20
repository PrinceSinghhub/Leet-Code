class Solution:
    def isToeplitzMatrix(self, matrix):
        d = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i - j in d and d[i - j] != matrix[i][j]:
                    return False
                else:
                    d[i - j] = matrix[i][j]

        return True


ans = Solution()
matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
print(ans.isToeplitzMatrix(matrix))