class Solution:
    def checkStraightLine(self, coordinates):

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for x, y in coordinates[2:]:
            if (y2 - y1) * (x - x1) != (x2 - x1) * (y - y1):
                return False

        return True

ans = Solution()
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(ans.checkStraightLine(coordinates))