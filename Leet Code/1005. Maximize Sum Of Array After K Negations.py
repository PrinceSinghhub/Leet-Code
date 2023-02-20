import heapq

class Solution(object):
    def largestSumAfterKNegations(self, S, K):
        heapq.heapify(S)
        for _ in range(K):
            v = heapq.heappop(S)
            heapq.heappush(S, -v)
        return sum(S)

ans = Solution()
nums = [4,2,3]
k = 1
print(ans.largestSumAfterKNegations(nums,k))