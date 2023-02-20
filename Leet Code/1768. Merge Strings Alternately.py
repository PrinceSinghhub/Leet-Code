class Solution:
    def mergeAlternately(self, word1, word2):

        if len(word1) == len(word2):

            ans = ''
            for i in range(len(word1)):
                ans += word1[i]
                ans += word2[i]

            return ans
        else:

            L1 = len(word1)
            L2 = len(word2)

            ans = ''
            if L1 > L2:

                last = word1[L2:]

                for i in range(L2):
                    ans += word1[i]
                    ans += word2[i]

                ans += last
                return ans


            else:
                last = word2[L1:]
                for i in range(L1):
                    ans += word1[i]
                    ans += word2[i]

                ans += last
                return ans


ans = Solution()
word1 = "abc"
word2 = "pqr"
print(ans.mergeAlternately(word1,word2))