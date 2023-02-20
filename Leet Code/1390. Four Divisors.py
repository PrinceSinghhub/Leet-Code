import math
class Solution:
    def sumFourDivisors(self, nums):

        s = 0
        for i in nums:
            r = i + 1
            c = 2
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    if (i / j == j):
                        c += 1
                        r += j
                    else:
                        c += 2
                        r += j + int(i / j)
            print(c, r)
            if c == 4:
                s += r
        return s

#         def divisior(digit):

#             div = [i for i in range(1,digit+1) if digit%i == 0]

#             return div

#         ans = 0

#         for i in nums:
#             res = divisior(i)
#             if len(res) == 0 or len(res) < 4:
#                 continue
#             elif len(res) == 4:
#                 ans+=sum(res)

#             elif len(res) > 4:
#                 ans+=sum(res[0:4])

#         return ans


ans = Solution()
nums = [21,4,7]
print(ans.sumFourDivisors(nums))