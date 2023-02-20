class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        i = 0
        count = 1

        for j in range(1, len(intervals)):

            if intervals[j][0] >= intervals[i][1]:
                count += 1
                i = j
        return len(intervals) - count

ans = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(ans.eraseOverlapIntervals(intervals))