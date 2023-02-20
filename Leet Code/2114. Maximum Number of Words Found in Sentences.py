class Solution:
    def mostWordsFound(self, sentences):

        ans = []
        for i in sentences:
            temp = 0
            for j in i:
                if j == " ":
                    temp += 1
            temp += 1
            ans.append(temp)

        return max(ans)

ans = Solution()
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(ans.mostWordsFound(sentences))