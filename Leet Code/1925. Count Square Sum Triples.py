import math
class Solution:
    def countTriples(self, n):
        res = 0

        for i in range(1, n):
            for j in range(i + 1, n):
                s = math.sqrt(i * i + j * j)
                if int(s) == s and s <= n:
                    res += 2

        return res


ans = Solution()
n = 5
print(ans.countTriples(n))