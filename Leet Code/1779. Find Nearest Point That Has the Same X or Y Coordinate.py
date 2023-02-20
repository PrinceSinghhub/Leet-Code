class Solution:
    def nearestValidPoint(self, x, y, points):
        def valid(t):
            i, (x1, y1) = t
            return x1 == x or y1 == y

        def key(t):
            i, (x1, y1) = t
            d = abs(x - x1) + abs(y - y1)
            return d, i

        matches = list(filter(valid, enumerate(points)))
        if not matches:
            return -1

        return next(i for i, p in sorted(matches, key=key))

ans = Solution()
x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
print(ans.nearestValidPoint(x,y,points))