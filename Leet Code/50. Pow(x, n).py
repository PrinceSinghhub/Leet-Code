import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return math.pow(x, n)


ans = Solution()

x = 2
n = 10
print(ans.myPow(x,n))