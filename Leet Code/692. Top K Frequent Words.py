import heapq

from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        dic = Counter(words)

        heap = [(-j, i) for i, j in dic.items()]
        print(heap)

        heapq.heapify(heap)

        print(heap)

        ans = [heapq.heappop(heap)[1] for _ in range(k)]
        print(ans)

        return ans
ans = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(ans.topKFrequent(words,k))