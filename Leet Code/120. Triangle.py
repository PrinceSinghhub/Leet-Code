class Solution:
    # def helper(self, arr, start, end):
    #     Min = min(arr[start:end + 1])
    #     Index = arr.index(Min)
    #
    #     return [Min, Index]
    #
    # def minimumTotal(self, triangle):
    #
    #
    #     arr = []
    #     arr.append(triangle[0][0])
    #
    #     row = 1
    #     start = 0
    #     end = start + 1
    #     while row < len(triangle):
    #         ans = self.helper(triangle[row], start, end)
    #         start = ans[1]
    #         arr.append(ans[0])
    #         row += 1
    #
    #     return sum(arr)

    # using DP
    def minimumTotal(self, triangle):



        for i in range(len(triangle) - 1, 0, -1):

            # find the smaller near num in the lower line and add it to the upper line
            for j in range(i):
                triangle[i - 1][j] = triangle[i - 1][j] + min(triangle[i][j], triangle[i][j + 1])
        # the top point will be the shortest length.
        return triangle[0][0]

ans = Solution()
nums = [[3],[2,5],[7,9,4],[8,6,5,3],[2,1,3,7,5]]
print(ans.minimumTotal(nums))





