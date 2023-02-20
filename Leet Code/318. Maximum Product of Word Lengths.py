class Solution:
    def maxProduct(self, words):
        n = len(words)
        value = [0] * n
        ans = 0
        for i in range(n):
            for j in words[i]:
                value[i] |= 1 << (ord(j) - 97)
        for i in range(n):
            for j in range(i + 1, n):
                if value[i] & value[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))

        print(value)
        return ans


ans = Solution()
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(ans.maxProduct(words))
