class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            LHS = n & 1
            reverseLHS = LHS << (31 - i)
            res = res | reverseLHS
            n = n >> 1

        return res

ans = Solution()
n =11111111111111111111111111111101
print(ans.reverseBits(n))