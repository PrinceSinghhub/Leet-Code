
class Solution:
    def maxPoints(self, points):
        count = {}
        for p1, p2 in combinations(map(tuple, points), 2):
            m = float("inf") if p1[0]==p2[0] else (p1[1]-p2[1])/(p1[0]-p2[0])   #Slope of line (infinity if slope is undefined)
            b = p1[0] if p1[0]==p2[0] else p1[1]-m*p1[0]                        #Y-intercept (X-intercept if slope is undefined)
            if (m, b) in count: count[(m, b)] |= set([p1, p2])                  #Add points to the lines set
            else: count[(m, b)] = set([p1, p2])                                 #Create a new line with given points
        return max([1]+[len(count[x]) for x in count])


ans = Solution()
points = [[1, 1], [2, 2], [3, 3]]
print(ans.maxPoints(points))