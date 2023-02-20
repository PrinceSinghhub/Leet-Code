class Solution:
    def minDistance(self, word1, word2):

        curr = [0] * (len(word2) + 1)
        prev = [0] * (len(word2) + 1)

        print(curr)
        print(prev)

        for i in reversed(range(len(word1))):
            for j in reversed(range(len(word2))):
                if word1[i] == word2[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(prev[j], curr[j + 1])
            curr, prev = prev, curr

        print(curr)
        print(prev)

        return len(word1) + len(word2) - 2 * prev[0]

ans  = Solution()
word1 = "sea"
word2 = "eat"
print(ans.minDistance(word1,word2))