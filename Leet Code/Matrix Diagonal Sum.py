# https://leetcode.com/problems/matrix-diagonal-sum/
class Solution(object):
    def diagonalSum(self, mat):

         # todo brouteforce approch
        L = (len(mat)-1) % 2

        # if(L==0):
        #     f = []
        #     # todo for front
        #     for i in range(len(mat)):
        #         f.append(mat[i][i])
        #
        #     # todo for back
        #     mid = int((len(mat)-1)/2)
        #
        #     row = 0
        #     for i in range(len(mat)-1,-1,-1):
        #         if i == mid:
        #             row+=1
        #             continue
        #         else:
        #             f.append(mat[row][i])
        #             row+=1
        #
        #     return sum(f)
        #
        # else:
        #     f =[]
        #     for i in range(len(mat)):
        #         f.append(mat[i][i])
        #
        #     row = 0
        #     for i in range(len(mat) - 1, -1, -1):
        #         f.append(mat[row][i])
        #         row+=1
        #
        #     return sum(f)

        # todo optimixe code
        ans = []

        for i in range(len(mat)):
            ans.append(mat[i][i])

        row = 0
        for i in range(len(mat) - 1, -1, -1):
            ans.append(mat[row][i])
            row += 1

        if(L==0):
            mid = int((len(mat)-1) / 2)
            ans = sum(ans)-mat[mid][mid]
            return ans
        else:
            return sum(ans)


a = Solution()
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(a.diagonalSum(mat))
