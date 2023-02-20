class Solution:
    def wordPattern(self, pattern, s):
        li = s.split(' ')
        di = {}
        if len(li) != len(pattern):
            return False

        for i, val in enumerate(pattern):
            if val in di and di[val] != li[i]:
                return False
            elif val not in di and li[i] in di.values():
                return False
            elif val not in di:
                di[val] = li[i]

        return True

ans = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(ans.wordPattern(pattern,s))