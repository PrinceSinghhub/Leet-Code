# https://leetcode.com/problems/complement-of-base-10-integer/
class Solution:
    def bitwiseComplement(self, n):

        if n == 0:
            return 1

        res = 0
        index = 0
        while n > 0:
            if n & 1 != 1:
                res = res | (1<<index)
            n = n >> 1
            index+=1
        return res

ans = Solution()
n = 10
print(ans.bitwiseComplement(n))
