from numpy import *


class Solution:
    def climbStairs(self, n):

        if n < 2:
            return n

        arr = zeros((n), int)
        arr[0] = 1
        arr[1] = 2

        for i in range(2, len(arr)):
            first = arr[i - 1]
            second = arr[i - 2]

            arr[i] = first + second
        return arr[n - 1]
ans = Solution()
n=3
print(ans.climbStairs(n))