class Solution:

    def calculate(self, s):

        ans = 0
        for i in s:
            ans += int(i)

        return str(ans)

    def digitSum(self, s, k):

        ans = ''

        if len(s) < k or len(s) == k:
            return s

        for i in range(0, len(s), k):

            if i + k >= len(s):

                temp = self.calculate(s[i::])
                ans += temp
            else:
                temp = self.calculate(s[i:i + k])
                ans += temp

        if len(ans) == k:
            return ans

        return self.digitSum(ans, k)

ans = Solution()
s = "11111222223"
k = 3
print(ans.digitSum(s,k))