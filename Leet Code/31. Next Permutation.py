''''class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        i = j = len(nums)-1

        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return

        while nums[j] <= nums[i-1]:
            j -= 1

        nums[i-1], nums[j] = nums[j], nums[i-1]


        nums[i:]= nums[len(nums)-1:i-1:-1]

        return nums'''


class Solution:

    def reverse(self, arr, index1, n):

        while index1 < n:
            temp = arr[index1]
            arr[index1] = arr[n]
            arr[n] = temp
            index1 += 1
            n -= 1

        return arr

    def find1Index(self, arr, n):

        while n >= 0:
            if arr[n] < arr[n + 1]:
                return n
            n -= 1

        return 0

    def find2Index(self, arr, n, index1):

        while n >= 0:
            if arr[n] > arr[index1]:
                return n
            n -= 1
        return 0

    def nextPermutation(self, arr):

        temp = arr.copy()
        temp.sort()
        if arr == temp[::-1]:
            arr[:] = temp
            return arr

        n = len(arr) - 2
        Index1 = self.find1Index(arr, n)
        Index2 = self.find2Index(arr, n + 1, Index1)

        if Index1 == 0 and Index2 == 0:
            return arr[::-1]

        # swap the element
        temp = arr[Index1]
        arr[Index1] = arr[Index2]
        arr[Index2] = temp

        l = len(arr) - 1
        ans = self.reverse(arr, Index1 + 1, l)
        return ans


ans = Solution()
arr = [3,2,1]
print(ans.nextPermutation(arr))