import fractions
import math as m
class Solution:
    def gcdOfStrings(self, str1, str2):

        # if len(str1) == len(str2):
        #     if str1 == str2:
        #         return str1
        #     else:
        #         return ''
        # else:
        #     if len(str1) < len(str2):
        #         str1, str2 = str2, str1
        #     if str1[:len(str2)] == str2:
        #         return self.gcdOfStrings(str1[len(str2):], str2)
        #     else:
        #         return ''
        if (str1 + str2 == str2 + str1):
            gcd = m.gcd(len(str1), len(str2))

            return str1[:gcd]
        else:
            return ''
ans = Solution()
str1 = "ABCABC"
str2 = "ABC"
print(ans.gcdOfStrings(str1,str2))
