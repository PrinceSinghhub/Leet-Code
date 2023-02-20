class Solution:
    def numberOfSteps(self, num):

        ans = 0

        while num != 0:

            if num % 2 == 0:  # if num%2!=0
                num /= 2
            else:
                num -= 1

            ans += 1

        return ans

ans = Solution()
num = 14
print(ans.numberOfSteps(num))