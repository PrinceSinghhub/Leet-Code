class Solution:
    def removeDuplicates(self, s):

        stack = []

        for i in s:
            if len(stack) != 0 and stack[-1] == i:
                stack.pop()

            else:
                stack.append(i)

        ans = "".join(stack)
        return ans






ans = Solution()
s = "abbaca"
print(ans.removeDuplicates(s))