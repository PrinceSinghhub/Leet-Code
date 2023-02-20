class Solution:
    def addDigits(self, num):



        def res(param):
            ans = 0
            while param > 0:
                ans += param % 10
                param = param // 10
            return ans

        while True:
            ans = res(num)
            if len(str(ans)) == 1:
                return ans
            num = ans

        # one linear code
        # if num == 0:
        #     return 0
        # return num % 9 or 9


ans = Solution()
n = 98
print(ans.addDigits(n))