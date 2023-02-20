class Solution:
    def generateParenthesis(self, n):

        result = []
        stack = []

        def recursive(open, close):
            if (open == close == n):
                result.append("".join(stack))
                return

            if (open < n):
                stack.append('(')
                recursive(open + 1, close)
                stack.pop()

            if (close < open):
                stack.append(')')
                recursive(open, close + 1)
                stack.pop()

        recursive(0, 0)
        return result


ans  = Solution()
n = 3
print(ans.generateParenthesis(n))

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "AB"
print(word in board)