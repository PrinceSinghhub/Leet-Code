class Solution:
    def sumBase(self, n, k):
        count = 0

        while n > 0:
            count += (n % k)
            n = n // k

        return count


ans = Solution()
n = 34
k = 6
print(ans.sumBase(n,k))