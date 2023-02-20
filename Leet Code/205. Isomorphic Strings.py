class Solution:
    def isIsomorphic(self, s, t):

        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

        # mydic = []
        # mydic.append(s[0]+t[0])
        # for i in range(1,len(s)):
        #     pair = ""
        #     pair+=s[i]
        #     pair+=t[i]
        #     if len(mydic)==0:
        #         mydic.append(pair)
        #
        #     for i in mydic:
        #         item = i
        #         for k in item:
        #             if k in pair:
        #                 return False
        #     mydic.append(pair)
        #
        # return True


ans = Solution()
s = "egl"
t = "adl"
print(ans.isIsomorphic(s,t))


