class Solution(object):
    def addToArrayForm(self, num, k):

        string = ""
        List = [str(i) for i in num]
        for i in List:
            string += i

        res = str(int(string) + k)

        finAns = [int(i) for i in res]
        return finAns

r = Solution()
num = [9,9,9,9,9,9,9,9,9,9]
n = 1
print(r.addToArrayForm(num,n))



