class Solution(object):
    def numSpecial(self, mat):
        row,col,count,x = len(mat),len(mat[0]),0,[sum(col) for col in zip(*mat)]
        for i in range(row):
            for j in range(col):
                if mat[i][j]==1 and sum(mat[i])==1 and x[j]==1:
                    count+=1
        return count



ans = Solution()
mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
print(ans.numSpecial(mat))