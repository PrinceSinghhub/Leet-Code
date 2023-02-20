class Solution:
    def addTwoNumbers(self, l1,l2):
        l1 = l1[::-1]
        l2 = l2[::-1]
        ltos=""
        ltos1 = ""
        for i in l1:
            ltos+=str(i)
        for j in l2:
            ltos1+=str(j)
        total = str(int(ltos)+int(ltos1))
        total = total[::-1]
        res = []
        for i in total:
            res.append(int(i))
        return res


a = Solution()
n= [9,9,9,9,9,9,9]
m = [9,9,9,9]
print(a.addTwoNumbers(n,m))
