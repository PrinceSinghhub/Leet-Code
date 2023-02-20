class Solution:
    def maximumWealth(self, accounts):
        r=[]
        for i in accounts:
            s=sum(i)
            r.append(s)
        print(len(r))
        print(r)
        # r.sort()
        # fi = r[len(r)-1]
        # return fi

        for i in range(len(r)):
            result = 0
            eq=0
            for k in range(len(r)):


                if r[i]>r[k]:

                    result+=1

                if r[i] == r[k]:
                    pass
                else:
                    eq+=1


            if result == len(r)-1:
                return r[i]

            if eq == 0:
                return r[i]

accounts = [[2,8,7],[7,1,3],[1,9,5]]
x=Solution()
print(x.maximumWealth(accounts))