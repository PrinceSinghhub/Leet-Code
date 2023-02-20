# https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s):
        String = s.split()

        if String:
            return len(String[-1])

        return 0

ans = Solution()
s = "   fly me   to   the moon  "
print(ans.lengthOfLastWord(s))
