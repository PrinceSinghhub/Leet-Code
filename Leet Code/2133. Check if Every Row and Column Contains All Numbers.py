class Solution:
    def checkValid(self, matrix):
        lst = [0] * len(matrix)
        for i in matrix:
            if len(set(i)) != len(matrix):
                return False
            for j in range(len(i)):
                lst[j] += i[j]

        print(lst)
        return len(set(lst)) == 1
# class Solution:
#     def checkValid(self, matrix):

#         ans = set()

#         for i in matrix:
#             if len(set(i)) != len(matrix):
#                 return False

#             ans.add(sum(i))

#         if len(ans) == 1:
#             return True
#         return False

ans = Solution()
matrix = [[1,2,3],[3,1,2],[2,3,1]]
print(ans.checkValid(matrix))