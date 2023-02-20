class Solution(object):
    def totalMoney(self, n):

        remains = n % 7
        head = n // 7 + 1
        ans = 0

        for i in range(1, head):
            ans += sum([i for i in range(i, i + 7)])
        for i in range(head, head + remains):
            ans += i

        return ans


ans = Solution()
print(ans.totalMoney(20))