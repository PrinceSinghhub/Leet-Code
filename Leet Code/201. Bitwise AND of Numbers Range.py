class Solution:
    def rangeBitwiseAnd(self, left, right):

        if left == right:
            return right

        while left < right:
            right = right - (right & -right)
        return right

ans = Solution()
left = 5
right = 7
print(ans.rangeBitwiseAnd(left,right))
