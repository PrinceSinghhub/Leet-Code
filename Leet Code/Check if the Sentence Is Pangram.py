class Solution:
    def checkIfPangram(self, sentence):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        c = 0
        for i in alpha:
            if i in sentence:
                c+=1
        if(c==26):
            return True
        else:
            return False

        # todo optimize solution
        # aplha = set(sentence)
        # if(len(aplha)==26):
        #     return True
        # else:
        #     return False
r = Solution()
sentence =  "leetcode"
print(r.checkIfPangram(sentence))
