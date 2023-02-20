class Solution:
    def toLowerCase(self, s):

        ans = ""

        for i in s:
            if i.isupper():
                ans += i.lower()
            else:
                ans += i

        return ans

ans = Solution()

s = "Hello"
print(ans.toLowerCase(s))
