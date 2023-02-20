class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False
        elif n == 1:
            return True
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            elif n % 3 == 0:
                n = n / 3
            elif n % 5 == 0:
                n = n / 5
            else:
                return False

        return True

ans = Solution()
n = 6
print(ans.isUgly(n))