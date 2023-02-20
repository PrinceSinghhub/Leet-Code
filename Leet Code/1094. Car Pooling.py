# https://leetcode.com/problems/car-pooling/submissions/
class Solution:
    def carPooling(self, trips, capacity):

        Trip_Route = [0 for i in range(1001)]

        for passenger, start, end in trips:
            Trip_Route[start] += passenger
            Trip_Route[end] -= passenger

        carLoad = 0
        for i in range(len(Trip_Route)):
            carLoad += Trip_Route[i]
            if carLoad > capacity:
                return False
        return True
ans = Solution()
n = 5
trips = [[2, 1, 5], [3, 3, 7]]
print(ans.carPooling(trips,n))
