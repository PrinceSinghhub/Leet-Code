class Solution:
    def validMountainArray(self, arr):

        if len(arr) < 3:
            return False

        ans = 0

        for i in range(len(arr) - 1):

            if (arr[i] < arr[i + 1]) and (ans == 0 or ans == 1):
                ans = 1

            elif (arr[i] > arr[i + 1]) and (ans == 1 or ans == 2):
                ans = 2

            else:
                return False

        if ans == 2:
            return True
        else:
            return False


ans = Solution()
arr = [0,3,2,1]
print(ans.validMountainArray(arr))