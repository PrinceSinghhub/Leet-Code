class Solution:
    def deleteGreatestValue(self, grid):

        fnas = 0

        while len(grid[0]) != 0:

            ans = []

            for i in range(len(grid)):

                ele = max(grid[i])
                grid[i].remove(ele)
                ans.append(ele)

            fnas+=max(ans)

        return fnas



ans = Solution()

grid = [[4,3,2,1],[6,5,3,7],[8,3,4,2]]
print(ans.deleteGreatestValue(grid))

