class Solution:
    def check(self, matrix, target):

        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if matrix[mid] > target:
                end = mid - 1
            if matrix[mid] < target:
                start = mid + 1

            if matrix[mid] == target:
                return True
        return False

    def searchMatrix(self, matrix, target):

        for i in matrix:
            ans = self.check(i, target)
            if ans == True:
                return True
        return False

ans  = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(ans.searchMatrix(matrix,target))