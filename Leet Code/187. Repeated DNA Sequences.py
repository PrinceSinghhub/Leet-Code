import collections
class Solution:
    def findRepeatedDnaSequences(self, s):
        counter = collections.Counter(s[i:i+10] for i in range(0, len(s) - 9))
        return [key for key in counter if counter[key] > 1]


ans = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(ans.findRepeatedDnaSequences(s))