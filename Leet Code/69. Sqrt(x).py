import math


class Solution:
    def mySqrt(self, x):

        ans = math.sqrt(x)
        return int(ans)

ans = Solution()
x=8
print(ans.mySqrt(x))