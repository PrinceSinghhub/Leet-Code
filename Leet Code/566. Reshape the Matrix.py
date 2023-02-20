class Solution:
    def matrixReshape(self, mat, r, c):
        flat_list = []
        matrix = []

        for sublist in mat:
            for item in sublist:
                flat_list.append(item)

        if len(flat_list) != r * c:
            return mat
        else:
            for i in range(0, len(flat_list), c):
                matrix.append(flat_list[i:i + c])
            return matrix
ans = Solution()
mat = [[1,2],[3,4]]
r = 1
c = 4
print(ans.matrixReshape(mat,r,c))