from collections import Counter


class Solution:
    def rearrangeCharacters(self, s, target):
        c1, c2 = map(Counter, (target, s))

        print(c1, c2)

        arr = [c2[c] // c1[c] for c in target]

        return min(arr)

ans = Solution()
s = "ilovecodingonleetcode"
target = "code"
print(ans.rearrangeCharacters(s,target))