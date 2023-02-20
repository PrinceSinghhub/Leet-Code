class Solution:
    def findAnagrams(self, s, p):
        LS, LP, S, P, A = len(s), len(p), 0, 0, []
        if LP > LS: return []
        for i in range(LP): S, P = S + hash(s[i]), P + hash(p[i])
        if S == P: A.append(0)
        for i in range(LP, LS):
            S += hash(s[i]) - hash(s[i - LP])
            if S == P: A.append(i - LP + 1)
        return A

    #     ans = []
    #     L = len(p)
    #
    #     for i in range(len(s) - len(p)+1):
    #         check = s[i:i+L]
    #         a = self.checkAns(check,p)
    #         if a == True:
    #             ans.append(i)
    #
    #     return ans
    #
    # def checkAns(self, check,p):
    #
    #     arr = []
    #     for i in p:
    #         arr.append(i)
    #     ans = True
    #     for i in check:
    #         if i in arr:
    #             arr.remove(i)
    #             pass
    #
    #         else:
    #             ans = False
    #     if ans == True:
    #         return True
    #     return False

ans = Solution()
s = "cbaebabacd"
p = "abc"
print(ans.findAnagrams(s,p))