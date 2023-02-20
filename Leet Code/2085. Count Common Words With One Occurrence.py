class Solution:
    def countWords(self, words1, words2):

        count = 0

        for i in words1:
            if words1.count(i) == 1 and i in words2 and words2.count(i) == 1:
                count += 1

        return count


ans = Solution()
words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
print(ans.countWords(words1,words2))
