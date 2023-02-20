class Solution(object):
    def areOccurrencesEqual(self, s):
        check = set()

        for i in s:
            check.add(s.count(i))

        if len(check) == 1:
            return True

        return False

ans = Solution()
s = "abacbc"
print(ans.areOccurrencesEqual(s))