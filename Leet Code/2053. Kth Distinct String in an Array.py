class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """

        mydistint = []

        for i in arr:
            if arr.count(i) == 1:
                mydistint.append(i)

        print(mydistint)

        if len(mydistint) >= k:
            return mydistint[k - 1]

        return ""


ans = Solution()
arr = ["d","b","c","b","c","a"]
k = 2
print(ans.kthDistinct(arr,k))