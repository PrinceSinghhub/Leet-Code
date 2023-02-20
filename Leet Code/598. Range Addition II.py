class Solution:
    def maxCount(self,m, n, ops):
        # optimize code

        minCol = n
        minRow = m

        for i in ops:
            minRow = min(minRow, i[0])
            minCol = min(minCol, i[1])

        return minCol * minRow
        # myarr = [0] *(m*n)
        #
        # for i in ops:
        #     mul = i[0]*i[1]
        #
        #     for j in range(mul):
        #
        #         myarr[j]+=1
        #
        # return myarr.count(max(myarr))

ans = Solution()
n = 40000
m = 40000
ops = []
print(ans.maxCount(m,n,ops))