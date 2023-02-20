class Solution:
    def areAlmostEqual(self, s1, s2):

        if s1 == s2:
            return True

        check = 0

        for i, j in zip(s1, s2):
            if i != j:
                check += 1

        if sorted(s1) == sorted(s2) and check == 2:
            return True

        return False

ans = Solution()
s1 = "bank"
s2 = "kanb"
print(ans.areAlmostEqual(s1,s2))

n = 2002

