class Solution:
    def decodeString(self, string):

        nums = []
        strs = []
        num = ""
        s = ""
        for i, ch in enumerate(string):
            if ch.isdigit():
                num += ch
            elif ch == "[":
                nums.append(int(num))
                strs.append(s)
                num = ""
                s = ""
            elif ch == "]":
                s = strs.pop() + nums.pop() * s  # watchout, replacing with the same string
            else:
                s += ch
        return s

ans = Solution()
s = "3[a]2[bc]"
print(ans.decodeString(s))