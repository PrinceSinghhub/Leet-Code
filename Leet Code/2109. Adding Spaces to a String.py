class Solution:
    def addSpaces(self, s, spaces):

        s = list(s)
        ct = 0
        ln = len(s) + len(spaces)
        j = 0
        ans = []

        for i in range(len(s)):
            if i == spaces[j]:
                ans.append(' ')
                if j < len(spaces) - 1:
                    j += 1
            ans.append(s[i])
        return (''.join(ans))


#         new_string = ""

#         mylist = set(spaces)


#         for i in range(len(s)):
#             if i in mylist:
#                 new_string += " "

#             new_string += s[i]
#         return new_string


# bruteforce Approch
#         ans = ""
#         ans+=s[:spaces[0]] + " "

#         for j in range(1, len(spaces)):
#             ans+=s[spaces[j-1]:spaces[j]]+" "
#         ans+=s[spaces[-1]:]

#         return ans

ans = Solution()
s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
print(ans.addSpaces(s,spaces))