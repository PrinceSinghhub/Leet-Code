class Solution:
    def countConsistentStrings(self, allowed,words):

        count = 0
        for i in words:
            flag = True
            for string in i:

                if string in allowed:
                    continue
                else:
                    flag = False
                    break

            if flag == True:
                count += 1

        return count

ans = Solution()

allowed ="abcd"
word = ["a","b","c","ab","ac","bc","abccd","aabbcd","bcda","a","b","c","ab","ac","bc","a","b","c","ab","ac","bc","a","b","c","ab","ac","bcdaaad"]
print(ans.countConsistentStrings(allowed,word))

