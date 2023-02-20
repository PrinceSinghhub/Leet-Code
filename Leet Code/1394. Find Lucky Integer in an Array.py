class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        ans = []

        for i in arr:
            if arr.count(i) == i:
                ans.append(i)

        if len(ans) == 0:
            return -1
        return max(ans)

ans = Solution()
arr = [1,2,2,3,3,3]
print(ans.findLucky(arr))