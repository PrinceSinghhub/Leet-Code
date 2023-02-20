class Solution(object):
    def findTheDifference(self, s, t):

        first = sorted(s)
        second = sorted(t)

        ans = ""
        for i in second:
            if i in first:
                first.remove(i)
            else:
                ans += i
                break

        return ans

ans = Solution()
s = "abcd"
t = "abcde"
print(ans.findTheDifference(s,t))
