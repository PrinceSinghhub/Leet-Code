class Solution:
    def intervalIntersection(self, firstList, secondList):
        if firstList == [] or secondList == []:
            return []

        res = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            l = max(firstList[i][0], secondList[j][0])
            r = min(firstList[i][1], secondList[j][1])

            if l <= r :
                res.append([l, r])

            if firstList[i][1] < secondList[j][1]:
                i += 1

            else:
                j += 1

        return res

ans = Solution()
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
print(ans.intervalIntersection(firstList,secondList))