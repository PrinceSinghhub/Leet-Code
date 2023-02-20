class Solution(object):
    def rotate(self, matrix):

        ans = []

        for i in range(len(matrix)):
            temp = []

            for j in range(len(matrix)):
                temp.append(matrix[j][i])

            temp = temp[::-1]
            ans.append(temp)
        matrix[:] = ans
        return matrix

ans = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(ans.rotate(matrix))