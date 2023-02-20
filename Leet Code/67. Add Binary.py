class Solution:
    def addBinary(self, a, b):
        ans = str((bin(int(a, 2) + int(b, 2))))
        return ans[2:]

ans = Solution()
a = "101"
b = "111"
print(ans.addBinary(a,b))