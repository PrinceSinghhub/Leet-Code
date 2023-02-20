from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))

ans = Solution()
n = 4
k = 3
print(ans.combine(n,k))