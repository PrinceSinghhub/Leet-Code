# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
class Solution:
    def finalValueAfterOperations(self, operations):
        
        # myData = {"++x","X++","--X","X--"}
        
        ans = 0
        for i in operations:
            if i == "++X":
                ans+=1
            if i == "X++":
                ans+=1
            if i == "--X":
                ans-=1
            if i == "X--":
                ans-=1
        return ans

ans = Solution()
operations = ["++X","++X","X++"]
print(ans.finalValueAfterOperations(operations))
