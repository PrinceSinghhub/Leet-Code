class Solution:
    def findRotation(self, mat, target):

        for i in range(3):
            if mat == target:
                return True
            mat = [list(x[::-1]) for x in zip(*mat)]
            print(mat)
        return mat == target

        # for i in target:
        #     if i in mat:
        #         continue
        #     if i[::-1] in mat:
        #         continue
        #     else:
        #         return False
        # return True
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """

ans = Solution()
mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
# for x in zip(*mat):
#     print(x)
print(ans.findRotation(mat,target))
