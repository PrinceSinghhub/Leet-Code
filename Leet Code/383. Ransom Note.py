class Solution:
    def canConstruct(self, ransomNote, magazine):

        first = sorted(ransomNote)
        second = sorted(magazine)

        for i in second:
            if i in first:
                first.remove(i)
        if len(first) == 0:
            return True
        return False

ans = Solution()
ransomNote = "a"
magazine = "b"
print(ans.canConstruct(ransomNote,magazine))