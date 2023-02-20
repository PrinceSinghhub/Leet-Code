class Solution:
    def addToArrayForm(self, num,k):
        string = ""
        List = [str(i) for i in num]
        for i in List:
            string += i

        res = str(int(string) + k)

        finAns = [int(i) for i in res]
        return finAns

ans = Solution()
num = [1,2,0,0]
k = 34
print(ans.addToArrayForm(num,k))

