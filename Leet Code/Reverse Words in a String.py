class Solution:
    def reverseWords(self, s):
        r = s.split()
        r=r[::-1]
        output = " ".join(r)
        # return " ".join(s.split()[::-1])
        return output



d = " 3c      2zPeO dpIMVv2SG    1AM       o       VnUhxK a5YKNyuG     x9    EQ  ruJO       0Dtb8qG91w 1rT3zH F0m n G wU"
r = Solution()
print(r.reverseWords(d))

