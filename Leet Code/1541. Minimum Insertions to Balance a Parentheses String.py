class Solution:
    def minInsertions(self, s: str) -> int:

        lcounter = 0
        toadd = 0

        N = len(s)

        i = 0
        while i < N:
            if s[i] == '(':
                lcounter += 1
                i += 1
            else:
                if s[i:i + 2] == '))':
                    if lcounter > 0:
                        lcounter -= 1
                        i += 2
                    else:
                        toadd += 1
                        i += 2
                else:
                    if lcounter > 0:
                        toadd += 1
                        lcounter -= 1
                        i += 1
                    else:
                        toadd += 2
                        i += 1
        return toadd + lcounter * 2