class Solution:
    def subtractProductAndSum(self, n):
        b=str(n)
        mul = 1
        add = 0
        for i in b:
            mul = mul*int(i)
        for j in b:
            add =  add+int(j)
        res = mul - add
        return res
x=Solution()
n = 4421
print(x.subtractProductAndSum(n))


