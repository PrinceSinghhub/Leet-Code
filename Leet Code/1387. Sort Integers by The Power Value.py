class Solution:
    def getKth(self, lo, hi, k):
        nl=[]
        self.dp={}
        for i in range(lo,hi+1):
            val=self.solve(i)
            nl.append([i,val])
        nl.sort(key=lambda x:x[1])
        for i in range(len(nl)):
            if i==k-1:
                return nl[i][0]
    def solve(self,num):
        if num==1:
            return 0
        if num in self.dp:
            return self.dp[num]
        if num%2==0:
            self.dp[num]=self.solve(num//2)+1
            return self.dp[num]
        else:
            self.dp[num]=self.solve((3*num)+1)+1
            return self.dp[num]

ans = Solution()
lo = 12
hi = 15
k = 2
print(ans.getKth(lo,hi,k))