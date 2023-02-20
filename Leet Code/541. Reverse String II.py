class Solution:
    def reverseStr(self, s: str, k: int):
        rev = s[0:k]
        rev = rev[::-1]

        norev = s[k:len(s)]

        ans = ""

        ans += rev
        ans += norev

        return ans

ans = Solution()
s = "abcdefg"
k = 2
print(ans.reverseStr(s,k))
