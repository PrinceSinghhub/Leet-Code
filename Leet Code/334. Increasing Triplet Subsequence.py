class Solution:
    def increasingTriplet(self, nums):
        min1 = min2 = float("inf")
        for i, n in enumerate(nums):
            if min1 < min2 < n:
                return True
            elif n < min1:
                min1 = n
            elif min1 < n < min2:
                min2 = n
        return False

ans = Solution()
nums = [1,2,3,4,5]
print(ans.increasingTriplet(nums))