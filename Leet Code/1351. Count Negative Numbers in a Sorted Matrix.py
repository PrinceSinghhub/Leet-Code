class Solution:
    def countNegatives(self, grid):

        ans = 0
        for i in range(len(grid)):

            start = 0
            end = len(grid[i])-1

            while start <= end:
                mid = (start + end) // 2
                if grid[i][mid] < 0:
                    end = mid - 1
                else:
                    start = mid + 1
            a =  len(grid[i]) - start
            ans+=a

        return ans
ans =Solution()
grid = [[-1,-1]]

print(ans.countNegatives(grid))







