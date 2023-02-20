class Solution:
    def defangIPaddr(self, address):

        ans = ""
        for i in address:

            if i == ".":
                ans += "[.]"

            else:
                ans += i
        return ans

ans = Solution()
address = "1.1.1.1"
print(ans.defangIPaddr(address))
