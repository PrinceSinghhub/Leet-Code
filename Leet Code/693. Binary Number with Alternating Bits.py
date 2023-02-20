class Solution:
    def hasAlternatingBits(self, n):

        con = bin(n)[2::]

        for i in range(len(con) - 1):

            if con[i] == '1' and con[i + 1] == '0':
                continue

            elif con[i] == '0' and con[i + 1] == '1':
                continue

            else:
                return False

        return True


ans = Solution()
n = 125487789
print(ans.hasAlternatingBits(n))