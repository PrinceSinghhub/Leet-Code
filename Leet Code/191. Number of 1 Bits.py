class Solution:
    def hammingWeight(self, n):
        # convert = str(n)
        # return convert.count('1')
        ans = 0
        while n!=0:
            ans += n % 2
            n = n >> 1
        return ans

ans = Solution()
n = 11111111111111111111111111111101
print(ans.hammingWeight(n))