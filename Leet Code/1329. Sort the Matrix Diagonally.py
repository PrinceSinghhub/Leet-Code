class Solution:

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        count = [0] * 101
        for i in range(R + C - 1):
            x, y = max(0, R - 1 - i), max(0, i - (R - 1))
            for d in range(min(R - x, C - y)):
                count[mat[x + d][y + d]] += 1
            d = 0
            for j in range(1, 101):
                while count[j]:
                    mat[x + d][y + d] = j
                    count[j] -= 1
                    d += 1
        return mat

ans = Solution()
mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
print(ans.diagonalSort(mat))