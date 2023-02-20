class Solution(object):
    def reorderedPowerOf2(self, n):

        l = sorted(list(str(n)))
        for i in range(30):
            a = 2 ** i
            b = sorted(list(str(a)))
            if l == b:
                return True

        return False

ans = Solution()
n = 4
print(ans.reorderedPowerOf2(n))