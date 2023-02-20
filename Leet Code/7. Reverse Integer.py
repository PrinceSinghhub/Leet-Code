class Solution:
    def reverse(self, x):

        new_num = abs(x)
        num = 0
        while new_num:
            num = num * 10 + new_num % 10
            new_num = new_num // 10

        num = num if x == abs(x) else num * -1

        if num > -2 ** 31 and num < 2 ** 31 - 1:
            return num
        return 0
ans = Solution()
x = 1534236
print(ans.reverse(x))
