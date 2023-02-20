class Solution:

    def calculate(self, s: str) -> int:

        # Strip and replace all the spaces
        s = s.strip().replace(" ", "")

        # Evaluate
        def update(stack: List, curr: str, operator: str):
            if curr:
                if operator == "-":
                    stack.append(-1 * int(curr))
                elif operator == "*":
                    n = stack.pop()
                    m = int(curr)
                    stack.append(n * m)
                elif operator == "/":
                    n = stack.pop()
                    m = int(curr)
                    stack.append(int(n / m))
                else:
                    stack.append(int(curr))
            return

        # Function to evaluate current
        def evaluate(s: str, idx: int = 0):

            stack = []
            operator = ""
            curr = ""

            while idx < len(s):

                # next char
                char = s[idx]

                # End of current expression
                if char == ")":
                    break

                # If new expression, evaluate it first
                elif char == "(":
                    v, idx = evaluate(s, idx + 1)
                    update(stack, str(v), operator)

                # If digit keep on appending
                elif char.isdigit():
                    curr = curr + char

                else:  # update stack
                    update(stack, curr, operator)
                    operator = char
                    curr = ""

                # increment index
                idx = idx + 1

            # Update stack for last operation
            update(stack, curr, operator)

            return (sum(stack), idx)

        return evaluate(s)[0]

ans = Solution()
s = " 2-1 + 2 "
print(ans.calculate(s))