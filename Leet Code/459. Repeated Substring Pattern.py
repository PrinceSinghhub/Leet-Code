class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        n = len(s)
        sub = ''
        for i in range(n // 2):
            sub += s[i]
            k, r = divmod(n, i + 1)
            if r == 0 and sub * k == s:
                return True

        return False


ans = Solution()
print(ans)
s = "abab"
print(ans.repeatedSubstringPattern(s))