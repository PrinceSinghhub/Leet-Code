class Solution:
    def findLargestElement(self,nums):

        start = 0
        end = len(nums)-1

        MaxElement = -9999999999999

        while start <= end:

            mid = start+(end-start)//2

            if nums[mid]>MaxElement:
                MaxElement = nums[mid]
                start = mid+1

        return MaxElement
    def findans(self,nums):

        start = 0
        end = len(nums) - 1

        ans = 9999999999999999999

        while start<= end:

            mid = start+(end-start)//2

            if nums[mid]<ans:
                ans = nums[mid]
                end = mid-1
        return ans

    def FindPivot(self,nums):
        start = 0
        end = len(nums) - 1

        while (start <= end):
            mid = start + (end - start) // 2

            # 4 cases over here
            if (mid < end and nums[mid] > nums[mid + 1]):
                return mid
            if (mid > start and nums[mid] < nums[mid - 1]):
                return mid - 1
            if (nums[start] >= nums[mid]):
                end = mid - 1
            if (nums[start] <= nums[mid]):
                start = mid + 1

        return -1

    def findMin(self, nums):
        # # also do wusing bibary search
        # return min(nums)
        pivot = self.FindPivot(nums)
        myarr = nums[pivot+1:]


        ans = self.findans(myarr)
        return ans





ans = Solution()
n = [4,5,6,7,0,1,2]
print(ans.findMin(n))