class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        arr = [float('inf')] + arr + [float('inf')]
        n, res = len(arr), 0

        while n>3:
            mi = min(arr)
            ind = arr.index(mi)

            if arr[ind-1]<arr[ind+1]:
                res+=arr[ind-1]*arr[ind]
            else:
                res+=arr[ind+1]*arr[ind]

            arr.remove(mi)
            n = len(arr)

        return res