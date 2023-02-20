class Solution:
    def canMakeArithmeticProgression(self, arr):

        arr.sort()

        diff = abs(arr[0] - arr[1])

        for i in range(1, len(arr)):

            if abs(arr[i] - arr[i - 1]) != diff:
                return False

        return True

ans = Solution()
arr = [3,5,1]
print(ans.canMakeArithmeticProgression(arr))
