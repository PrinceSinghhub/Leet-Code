# https://leetcode.com/problems/reshape-the-matrix/
from numpy import *
class Solution:
    def matrixReshape(self, mat,r,c):

        ans = zeros((r,c),int)

        if r>1:
            a = 0

            while a<len(mat):
                index = 0
                for i in range(len(mat[a])):
                    ans[a][index] = mat[a][i]
                    index += 1
                a += 1
            return ans
        else:
            a = 0
            index = 0
            while a<len(mat):
                for i in range(len(mat[a])):
                    ans[r-1][index] = mat[a][i]
                    index += 1
                a += 1

            return ans

ans = Solution()

mat = [[1,2],[3,4]]; r = 2; c = 4
print(ans.matrixReshape(mat,r,c))
