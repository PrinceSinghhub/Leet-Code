# https://leetcode.com/problems/implement-strstr/
class Solution:
    def strStr(self, haystack,needle):
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
    
        return -1
ans = Solution()
haystack = "a"
needle = "a"
print(ans.strStr(haystack,needle))

