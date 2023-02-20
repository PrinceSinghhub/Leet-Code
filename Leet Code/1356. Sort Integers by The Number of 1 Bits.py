class Solution:
    def sortByBits(self, arr):
        arr = [(bin(i).count('1'), i) for i in arr]
        arr.sort()

        ans = []

        for i in arr:
            ans.append(i[1])

        return ans

ans = Solution()
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(ans.sortByBits(arr))