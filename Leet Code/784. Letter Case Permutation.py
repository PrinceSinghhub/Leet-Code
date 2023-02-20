class Solution(object):
    def letterCasePermutation(self, S):

        digits = {str(x) for x in range(10)}
        A = ['']
        for c in S:
            B = []
            if c in digits:
                for a in A:
                    B.append(a+c)
            else:
                for a in A:
                    B.append(a+c.lower())
                    B.append(a+c.upper())
            A=B
        return A

ans = Solution()
s = "a1b2"
print(ans.letterCasePermutation(s))