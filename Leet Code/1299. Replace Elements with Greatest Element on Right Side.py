class Solution:
    def replaceElements(self, arr):

        L = len(arr)-1
        ans = []
        for i in range(len(arr)):
            if i == L:
                ans.append(-1)
            else:
                part = arr[i+1:]
                ans.append(max(part))

        return ans

ans = Solution()
arr = [17,18,5,4,6,1]
print(ans.replaceElements(arr))
