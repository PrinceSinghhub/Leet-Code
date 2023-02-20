class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):

        res = 0
        arr2.sort()
        m = len(arr2)
        for i in arr1:
            low, high = 0, m - 1
            while high - low > 1:
                mid = (low + high) // 2
                if i > arr2[mid]:
                    low = mid
                else:
                    high = mid
            if min(abs(arr2[high] - i), abs(arr2[low] - i)) > d:
                res += 1
        return res


ans = Solution()
arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
print(ans.findTheDistanceValue(arr1,arr2,d))
