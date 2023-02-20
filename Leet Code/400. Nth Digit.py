class Solution:
    def findNthDigit(self, n):
        lower = upper = 1
        while n > (9 * upper * lower):
            n = n - (9 * upper * lower)
            lower += 1
            upper *= 10
        div1, div2 = divmod(n - 1, lower)

        ans = int(str(upper + div1)[div2])

        print(ans)

        return ans

#         inf = []

#         ans = []

#         for i in range(1,n+1):
#             inf.append(i)


#         for i in inf:

#             if len(ans) == n:
#                 break

#             con = str(i)
#             if len(con) > 1:

#                 for j in con:
#                     ans.append(int(j))

#             else:
#                 ans.append(i)

#         print(ans)

#         return ans[-1]

ans = Solution()
n = 100
print(ans.findNthDigit(n))
