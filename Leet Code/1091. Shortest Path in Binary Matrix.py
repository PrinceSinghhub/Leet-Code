class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1:
            return -1
        q = [(0, 0, 1)]
        while len(q) > 0:
            x, y, d = q.pop(0)
            if x == rows-1 and y == cols-1:
                return d
            for a, b in ((x-1, y-1), (x+1, y+1), (x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y+1), (x+1, y-1)):
                if 0 <= a < rows and 0 <= b < cols and grid[a][b] == 0:
                    grid[a][b] = 1
                    q.append((a, b, d+1))

        return -1

ans = Solution()
grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(ans.shortestPathBinaryMatrix(grid))