class Solution:
    def solve(self, board):

        m = len(board)
        n = len(board[0])

        # Edge cases: If num rows or cols <= 2 then "O" can never become "X"
        if m <= 2 or n <= 2:
            return board

        # Mark all connected "O" starting from any border as 1
        def helper(r, c, m, n, board):

            self.visited[r][c] = 1
            if r - 1 >= 0 and board[r - 1][c] == "O" and self.visited[r - 1][c] == 0:
                helper(r - 1, c, m, n, board)
            if r + 1 < m and board[r + 1][c] == "O" and self.visited[r + 1][c] == 0:
                helper(r + 1, c, m, n, board)
            if c - 1 >= 0 and board[r][c - 1] == "O" and self.visited[r][c - 1] == 0:
                helper(r, c - 1, m, n, board)
            if c + 1 < n and board[r][c + 1] == "O" and self.visited[r][c + 1] == 0:
                helper(r, c + 1, m, n, board)

        # Create visited matrix similar in dim to input board
        self.visited = [[0 for j in range(n)] for i in range(m)]

        # Traverse edge rows and look for "O". If "O" is found, dfs and find all connected "O"s
        edge_r = [0, m - 1]
        for r in edge_r:
            for c in range(0, n):
                if self.visited[r][c] == 0 and board[r][c] == "O":
                    helper(r, c, m, n, board)

        # Same as above but for edge columns
        edge_c = [0, n - 1]
        for r in range(0, m):
            for c in edge_c:
                if self.visited[r][c] == 0 and board[r][c] == "O":
                    helper(r, c, m, n, board)

        # Loop thru remaining rows/cols and if not visited, set "O" to "X"
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if board[r][c] == "O" and self.visited[r][c] == 0:
                    board[r][c] = "X"

ans = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(ans.solve(board))