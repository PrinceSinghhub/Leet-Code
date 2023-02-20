# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s):

        arr = []
        for i in s:
            if i in ['(','{','[']:
                arr.append(i)

            elif i == ')' and len(arr)!=0 and arr[-1]=='(':
                arr.pop()

            elif i == '}' and len(arr)!=0 and arr[-1]== '{':
                arr.pop()

            elif i == ']' and len(arr)!=0 and arr[-1]=='[':
                arr.pop()

            else:
                return False
        if len(arr)==0:
            return True

ans = Solution()
s = "()"
print(ans.isValid(s))