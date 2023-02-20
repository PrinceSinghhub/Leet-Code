class Solution:
    def isHappy(self, n):
        ans = 0
        while ans != 1 and n != 4:
            ans = 0
            while n > 0:
                temp = n % 10
                ans += (temp * temp)
                n = n // 10
            n = ans
        if ans == 1:
            return True
        return False
ans = Solution()
n = 2
print(ans.isHappy(n))
