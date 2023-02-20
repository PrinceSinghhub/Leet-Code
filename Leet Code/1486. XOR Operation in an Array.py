class Solution:
    def xorOperation(self, n, start):

        arr = []

        for i in range(n):
            ans = start + 2 * i
            arr.append(ans)
        print(arr)

        ans = arr[0]

        for i in range(1, len(arr)):
            ans = ans ^ arr[i]

        return ans


ans =  Solution()
n = 5
start = 0
print(ans.xorOperation(n,start))