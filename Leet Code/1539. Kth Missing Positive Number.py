class Solution(object):
    def findKthPositive(self, arr, k):

        # arr = list(set(arr))
        # arr.sort()
        #
        # for i in range(1, len(arr) + k + 1):
        #     if i not in arr:
        #         k-=1
        #
        #     if k == 0:
        #         return i

       # todo usinig Binary Search
       start = 0
       end = len(arr)-1

       while start<=end:
           mid = start+(end-start)//2
           if arr[mid]-mid-1<k:
               start = mid+1

           else:
               end = mid-1
       return start+k




ans = Solution()
arr = [3,5,8,9,10]
k = 7
print(ans.findKthPositive(arr,k))