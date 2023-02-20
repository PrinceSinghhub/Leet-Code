class Solution:
    def balancedStringSplit(self, s):

        r, l = 0, 0
        count = 0
        for i in s:
            if i == 'R':
                r += 1
            else:
                l += 1
            if r == l:
                count += 1
                r = 0
                l = 0

        return count


ans = Solution()
s = "RLRRLLRLRL"
print(ans.balancedStringSplit(s))
