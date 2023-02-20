class Solution(object):
    # hard level question on leetcode: https://leetcode.com/problems/find-in-mountain-array/
    def findInMountainArray(self, target, mountain_arr):

        PeakValue = self.GreatestNumber(mountain_arr)
        AssendingSearch = self.OrderAgnosist(mountain_arr,target,0,PeakValue)

        if AssendingSearch != -1:
            return AssendingSearch
        else:
            DessendingSearch = self.OrderAgnosist(mountain_arr, target,PeakValue+1, len(mountain_arr)-1)
            return DessendingSearch

    def GreatestNumber(self, nums):

        start = 0
        end = len(nums) - 1

        while start < end:

            mid = start + (end - start) // 2

            if (nums[mid] > nums[mid + 1]):
                end = mid

            if (nums[mid] < nums[mid + 1]):
                start = mid + 1

        return start  # also return end point becouse start and end are at same point

    def OrderAgnosist(self, arr, element, start, end):

        if (arr[start] < arr[end]):


            while (start <= end):
                mid = start + (end - start) // 2

                if (element > arr[mid]):
                    start = mid + 1

                if (element < arr[mid]):
                    end = mid - 1

                if (arr[mid] == element):
                    return mid
        else:

            while (start <= end):
                mid = start + (end - start) // 2

                if (element > arr[mid]):
                    end = mid - 1

                if (element < arr[mid]):
                    start = mid + 1

                if (arr[mid] == element):
                    return mid

        return -1

ans = Solution()
array = [1,2,3,4,5,3,1]; target = 3
print(ans.findInMountainArray(target,array))
