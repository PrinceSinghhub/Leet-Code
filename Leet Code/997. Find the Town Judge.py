# class Solution:
#     def findJudge(self, n, trust):
#
#
#         for i in range(len(trust)):
#             TP = trust[i][1]
#             ans = 0
#             for j in range(len(trust)):
#                 if trust[j][0] == TP:
#                     ans = -1
#             if ans == 0:
#                 return TP
#             else:
#                 pass
#         return -1
class Solution:
    def findJudge(self, n,trust):

        Trust_People = [0] * (n + 1)
        for a, b in trust:
            Trust_People[a] -= 1
            Trust_People[b] += 1

        print(Trust_People)
        for i in range(1, n + 1):
            if Trust_People[i] == n - 1:
                return i
        return -1

ans = Solution()
n = 2
trust = [[1,2]]
print(ans.findJudge(n,trust))