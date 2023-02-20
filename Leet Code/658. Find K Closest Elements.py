import heapq


class Solution(object):

    def findClosestElements(self, arr, k, x):
        heap = []
        res = []
        # nlogn
        for i in range(len(arr)):  # n
            heap.append((abs(x - arr[i]), arr[i]))
        # heapify() - logn
        # Means smallest at the first position - all times...
        heapq.heapify(heap)
        # nlogn
        for _ in range(k):  # n
            # heappop() - logn
            # Append the values accordingly...
            res.append(heapq.heappop(heap)[1])
        return sorted(res)

ans = Solution()
arr = [1,2,3,4,5]
k = 4
x = 3
print(ans.findClosestElements(arr,k,x))
