class Solution:
    def checkIfExist(self, arr):

        for i in range(len(arr)):
            if 2 * arr[i] in arr and arr.index(2 * arr[i]) != i:
                return True
        return False

ans =Solution()
arr = [10,2,5,3]
print(ans.checkIfExist(arr))