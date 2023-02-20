class Solution:
    def isSameAfterReversals(self, num):

        original = num
        rev = 0

        while num > 0:
            rev = (rev * 10) + (num % 10)
            num = num // 10

        rev1 = 0
        print(rev1)
        while rev > 0:
            rev1 = (rev1 * 10) + (rev % 10)
            rev = rev // 10

        if rev1 == original:
            return True

        print(rev1)
        return False

ans = Solution()
num = 256
print(ans.isSameAfterReversals(num))