class Solution:

    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):

            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return list(d.values())

ans = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(ans.groupAnagrams(strs))