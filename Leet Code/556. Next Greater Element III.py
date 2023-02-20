from bisect import bisect

class Solution(object):
    def nextGreaterElement(self, n):

        s = str(n)
        for i in range(len(s) - 2, -1, -1):
            if s[i] < s[i + 1]:
                break
        else:
            return -1

        r = s[:i:-1]
        j = bisect.bisect_left(r, chr(ord(s[i]) + 1))
        n = int(s[:i] + r[j] + r[:j] + s[i] + r[j + 1:])

        return -1 if n >> 31 else n

ans = Solution()
print(ans.nextGreaterElement(12))