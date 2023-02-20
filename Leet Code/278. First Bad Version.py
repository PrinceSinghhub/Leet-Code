class Solution:
    def firstBadVersion(self, n):

        first = 0
        last = n - 1
        while first <= last:
            mid = first + (last - first) // 2
            if isBadVersion(mid) == False:
                first = mid + 1
            else:
                last = mid - 1
        return first