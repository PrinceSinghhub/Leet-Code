class Solution:
    def allCellsDistOrder(self, R, C, r0, c0):
        def helpp(y):
            return (abs(r0 - y[0]) + abs(c0 - y[1]))
        res = []
        i = -1
        j = -1
        for row in range(R):
            i += 1
            j = -1
            for col in range(C):
                j += 1
                res.append([i,j])
        res.sort(key = helpp)
        return res


ans = Solution()
rows = 1
cols = 2
rCenter = 0
cCenter = 0
print(ans.allCellsDistOrder(rows,cols,rCenter,cCenter))