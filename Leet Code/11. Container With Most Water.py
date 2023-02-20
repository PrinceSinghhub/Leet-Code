class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        Max = -1
        while (l <= r):
            x = min(height[l], height[r]) * (r - l)
            Max = max(x, Max)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        print(Max)
        return Max
ans = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(ans.maxArea(height))