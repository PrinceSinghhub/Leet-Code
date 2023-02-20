class Solution1:
    def merge(self, nums1,m,nums2,n):
        nums1[m:] = nums2
        nums1.sort()


# another methode
class Solution:

    def twoSortedArrays(self, arr1, arr2):

        if len(arr1) == 0:
            return arr2

        if len(arr2) == 0:
            return arr1

        m = len(arr1)
        for i in range(m):

            if arr1[i] == 0:
                arr1[i] = float('inf')

        for i in range(m):

            if arr1[i] > arr2[0]:
                temp = arr1[i]
                arr1[i] = arr2[0]
                arr2[0] = temp

                arr2.sort()

        while float('inf') in arr1:
            arr1.remove(float('inf'))
            arr1.append(0)
            arr1.sort()

        return arr1

    def merge(self, nums1, m, nums2, n):

        ans = self.twoSortedArrays(nums1, nums2)

        return ans

ans = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(ans.merge(nums1,m,nums2,n))
