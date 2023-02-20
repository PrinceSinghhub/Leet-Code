class Solution:
    def isPalindrome(self, x):
        Str = str(x)
        if Str == Str[::-1]:
            return True
        return False
ans = Solution()
print(ans.isPalindrome(222))