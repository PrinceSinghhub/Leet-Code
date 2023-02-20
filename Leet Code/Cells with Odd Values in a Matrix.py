from numpy import*
class Solution:
    def oddCells(self, m, n, indices):

        a = zeros((m, n), int)
        for i in indices:
            for j in range(n):
                r=i[0]
                a[r][j] += 1

            for k in range(m):
                r=i[1]
                a[k][r] += 1

        count = 0
        for i in a:
            for j in i:
                if j % 2 != 0:
                    count += 1

        return count


b = [[0, 1], [1,1]]
r = Solution()
print(r.oddCells(2,3,b))