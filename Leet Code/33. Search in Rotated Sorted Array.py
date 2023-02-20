class Solution:
    def search(self, nums, target):

        res = self.SearchElement(nums,target)
        return res

    def SearchElement(self,nums, target):

        pivot = self.FindPivot(nums)

        if(pivot == -1):
            return self.BinarySearch(nums,target,0,len(nums)-1)

        if(nums[pivot] == target):
            return pivot

        if(target>=nums[0]):
            return self.BinarySearch(nums,target,0,pivot-1)
        if(target<nums[0]):
            return self.BinarySearch(nums,target,pivot+1,len(nums)-1)

    def FindPivot(self, nums):

        start = 0
        end = len(nums)-1

        while(start<=end):
            mid = start+(end-start)//2

        # 4 cases over here
            if(mid < end and nums[mid]>nums[mid+1]):
                return mid
            if(mid > start and nums[mid]<nums[mid-1]):
                return mid-1
            if(nums[start]>=nums[mid]):
                end = mid-1
            if(nums[start]<=nums[mid]):
                start = mid+1

        return -1

    def BinarySearch(self, nums, target, start, end):

        while(start<=end):
            mid = start+(end-start)//2

            if(target>nums[mid]):
                start = mid+1
            if(target<nums[mid]):
                end = mid-1
            if(target==nums[mid]):
                return mid

        return -1

ans = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(ans.search(nums,target))
