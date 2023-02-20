class Solution:
    def generate(self, numRows):

        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        Tri = [[1]]

        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(Tri[i - 1][j - 1] + Tri[i - 1][j])
            row.append(1)
            Tri.append(row)
        return Tri


ans = Solution()
n = 3
print(ans.generate(n))