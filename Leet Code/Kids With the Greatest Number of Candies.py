class Solution:
    def kidsWithCandies(self, candies,extraCandies):
        Len=max(candies)
        res = []
        for i in candies:
            if(i+extraCandies>=Len):
                res.append(True)
            else:
                res.append(False)


        return res
candies = [2,3,5,1,3];extraCandies = 3
e = Solution()
print(e.kidsWithCandies(candies,extraCandies))

