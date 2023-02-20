class Solution:
    def countOdds(self, low, high):

        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        if low % 2 == 1 or high % 2 == 1:
            return (high - low) // 2 + 1

#         ans = 0
#         for i in range(low,high+1):

#             if  i%2!=0:
#                 ans+=1
#         return ans


ans = Solution()
low = 452315641
high = 985647512
print(ans.countOdds(low,high))