import collections
class Solution:
    def isAnagram(self, s, t):


        if len(s) == len(t):

            check = list(t)

            for i in s:
                if i in check:
                    check.remove(i)
                    continue
                else:
                    return False

            return True

        else:
            return False

        # # using module
        # first = collections.UserList(s)
        # second = collections.UserList(t)
        #
        #
        #
        #
        # if len(first)==len(second):
        #     for key in first:
        #         if key in second:
        #             second.remove(key)
        #             continue
        #     if len(second) == 0:
        #         return True
        #     return False
        # return False

ans = Solution()
s = "aacc"
t = "ccac"
print(ans.isAnagram(s,t))

