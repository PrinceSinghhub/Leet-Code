class Solution(object):
    def findPeakGrid(self, mat):
        m, n = len(mat), len(mat[0])

        def binarySearch(row):
            l, r = 0, n - 1

            while l <= r:
                mid = l + (r - l) // 2
                left = -1 if mid == 0 else mat[row][mid - 1]
                right = -1 if mid == n - 1 else mat[row][mid + 1]
                top = -1 if row == 0 else mat[row - 1][mid]
                bottom = -1 if row == m - 1 else mat[row + 1][mid]

                if left < mat[row][mid] > right and top < mat[row][mid] > bottom:
                    return mid
                if left >= right:
                    r = mid - 1
                else:
                    l = mid + 1

            return None

        for row in range(m):
            col = binarySearch(row)
            if col is not None: return [row, col]

        return []




ans = Solution()
mat = [[10,20,15],[21,30,14],[7,16,32]]
print(ans.findPeakGrid(mat))
