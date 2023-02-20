# https://leetcode.com/problems/flipping-an-image/
from numpy import *
class Solution:
    # brutforce approch
    def flipAndInvertImage(self, image):
        revArry = zeros((len(image),len(image)),dtype=int)

        row = 0
        for i in range(len(image)):
            collom = 0
            for j in range(len(image[i])-1,-1,-1):
                revArry[row][collom] = image[i][j]
                collom+=1

            row+=1

        for i in range(len(revArry)):
            for j in range(len(revArry[i])):

                if revArry[i][j] == 0:
                    revArry[i][j] = 1
                else:
                    revArry[i][j] = 0


        return revArry


ans  = Solution()
image =  [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(ans.flipAndInvertImage(image))