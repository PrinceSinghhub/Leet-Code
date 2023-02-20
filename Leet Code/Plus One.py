# https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits):

        L = len(digits) - 1

        while digits[L] == 9:
            digits[L] = 0
            L -= 1

        if L == -1:
            digits.insert(0, 1)

        else:
            digits[L] += 1

        return digits

ans = Solution()
a = [9,9]
print(ans.plusOne(a))