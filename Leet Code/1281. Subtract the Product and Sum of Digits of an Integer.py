class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add = 0
        mul = 1

        while n > 0:
            rem = n % 10
            add += rem
            mul *= rem
            n = n // 10

        return mul - add


ans = Solution()
n = 234
print(ans.subtractProductAndSum(n))