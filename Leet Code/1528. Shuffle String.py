class Solution:
    def restoreString(self, s, indices):

        mydic = {}
        a = {1: 1, 2: 5}
        print(a)

        StringIndex = 0
        arrIndex = 0

        while StringIndex < len(s):
            mydic[indices[arrIndex]] = s[StringIndex]
            StringIndex += 1
            arrIndex += 1

        ans = ""
        for i in range(len(indices)):
            ans += mydic[i]

        return ans

ans = Solution()
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(ans.restoreString(s,indices))
