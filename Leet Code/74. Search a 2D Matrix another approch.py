class Solution:
    def searchMatrix(self, matrix, target):

        for i in matrix:

            start = 0
            end = len(i) - 1

            while start <= end:

                mid = start + (end - start) // 2

                if i[mid] == target:
                    return True

                if target > i[mid]:
                    start = mid + 1

                if target < i[mid]:
                    end = mid - 1

        return False
ans  = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(ans.searchMatrix(matrix,target))