class Solution:
    def interpret(self, command):

        # paranCount = 0
        ans = ""

        for i in range(len(command)):

            if command[i] == '(' and command[i + 1] == ')':

                ans += 'o'

            elif command[i] == '(' and command[i + 1] != ')':

                res = "(al)"
                check = ""

                for i in range(i, len(command)):
                    if command[i] == ')':
                        check += command[i]
                        break
                    else:
                        check+=command[i]

                if res == check:
                    ans += "al"

            elif command[i] == "G":
                ans += "G"

        return ans

ans = Solution()
a = "(al)G(al)()()G"
print(ans.interpret(a))