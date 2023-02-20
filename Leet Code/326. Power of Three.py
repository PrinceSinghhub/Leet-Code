class Solution:
    def isPowerOfThree(self, n):

        if n == 0:
            return False

        while n != 1:

            if n % 3 != 0:
                return False

            n = n // 3

        return True

ans = Solution()
n = 27
print(ans.isPowerOfThree(n))