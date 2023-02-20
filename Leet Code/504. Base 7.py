class Solution:
    def convertToBase7(self, num):

        sign = ''
        if num == 0:
            return '0'
        if num < 0:
            sign = '-'
        else:
            sign = ''
        ans = ''
        num = abs(num)
        while num:
            ans += str(num % 7)
            num //= 7
        return sign + ans[::-1]

ans = Solution()
n = 100
print(ans.convertToBase7(n))