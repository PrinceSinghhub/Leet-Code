import collections
class Solution:
    def firstUniqChar(self, s):

        # bruteforce approch
        # for i in range(len(s)):
        #     if s.count(s[i]) > 1:
        #         continue
        #     return i
        # return -1

        # optimize code
        heap = collections.Counter(s)
        for key, value in enumerate(s):
            if heap[value] <= 1:
                return key
        return -1


ans = Solution()
s = "leetcode"
print(ans.firstUniqChar(s))