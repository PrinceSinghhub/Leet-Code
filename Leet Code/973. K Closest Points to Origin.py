import heapq


class Solution:
    def kClosest(self, points, k):

        heap = []

        for x, y in points:
            heapq.heappush(heap, (-(x * x + y * y), x, y))

            while len(heap) > k:
                heapq.heappop(heap)
        print(heap)
        ans = [[x, y] for d, x, y in heap]

        for i, j, k in heap:
            print(j)
        print(ans)
        return ans


ans = Solution()
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(ans.kClosest(points,k))