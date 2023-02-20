import collections
class Solution:
    def isValidSudoku(self, board):
        boardMap = collections.defaultdict(list)
        for x in range(9):
            for y in range(9):
                char = board[x][y]
                if char != '.':
                    if char in boardMap:
                        for pos in boardMap[char]:
                            if (pos[0] == x) or (pos[1] == y) or (pos[0] // 3 == x // 3 and pos[1] // 3 == y // 3):
                                return False
                    boardMap[char].append((x, y))

        return True

ans = Solution()
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(ans.isValidSudoku(board))

