from numpy import *
class Solution(object): #https://leetcode.com/problems/transpose-matrix/
    def transpose(self, matrix):

        # todo brouteforce approch
        # row = len(matrix)
        # collom = len(matrix[0])
        #
        # ans = zeros((collom,row),dtype=int)
        #
        # for i in range(row):
        #     for j in range(collom):
        #         ans[j][i] = matrix[i][j]
        #
        # return ans
        # todo optimize code
        res = list(zip(*matrix))
        return res

r = Solution()
matrix = [[1,2,3],[4,5,6]]
print(r.transpose(matrix))
