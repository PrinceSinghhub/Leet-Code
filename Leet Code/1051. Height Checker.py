class Solution:
    def heightChecker(self, heights):

        count = 0

        temp = heights.copy()
        temp.sort()
        for i in range(len(heights)):
            if heights[i]==temp[i]:
                continue
            else:
                count+=1
        return count


ans = Solution()
heights = [1,1,4,2,1,3]
print(ans.heightChecker(heights))
