class Solution:
    def relativeSortArray(self, arr1, arr2):

        ans = []

        for i in arr2:

            if i in arr1:

                for j in range(arr1.count(i)):
                    ans.append(i)

        remain = []

        for i in arr1:
            if i not in ans:
                remain.append(i)

        remain.sort()

        ans.extend(remain)

        return ans


ans = Solution()
arr1 = [1,2,4,5,8,7,4,6,5,9,8,5,3,2,5,5,4,7,8,5]
arr2 = [1,2,3,4,5,6,7]
print(ans.relativeSortArray(arr1,arr2))