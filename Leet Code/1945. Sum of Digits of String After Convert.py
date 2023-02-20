class Solution:
    def getLucky(self, s, k):
        s = int(''.join(str(ord(c) - 96) for c in s))
        print(s)
        for i in range(k):
            s_sum = 0
            while s:
                s_sum += s % 10
                s //= 10
            s = s_sum
        return s
ans = Solution()
s = "qhquvppzooyt"
k = 6
print(ans.getLucky(s,k))