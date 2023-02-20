class Solution:
    def freqAlphabets(self, s: str) -> str:
        x, i = '', 1
        while i < len(s)+1:
            if s[-i] != '#':
                x = chr(int(s[-i])+96) + x
                i += 1
            else:
                i += 1
                x = chr(int(s[-i-1:-i+1])+96) + x
                i += 2
        return x

ans = Solution()
s = "10#11#12"
print(ans.freqAlphabets(s))