class Solution:
# gfg question: https://ide.geeksforgeeks.org/tohKjeCMxw
    def ans(self, nums, target):

        '''first find the range of our chunk
            and start our search with box size 2'''
        start = 0
        end = 1

       # condition for our taget vale lie thar chunk or not

        while(target>nums[end]):
             temp = end+1 # our new start end point

             '''now double the sixe of chunk or box
                for chek lie our value or not
                formula = prevese end + sixeofBox*2'''

             end = end+(end-start+1)*2  # our new end  point
             start = temp

        res = self.FindIndex(nums,target,start,end)
        return res

    def FindIndex(self, nums, target, start, end):



        while(start<=end):
            mid = start+(end - start) // 2

            if(target>nums[mid]):
                start = mid+1

            if (target < nums[mid]):
                end = mid - 1

            if (target == nums[mid]):
                return mid

        return -1 #means ans are not found

r = Solution()

myarr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170, 190, 200, 210, 220, 250, 290] # this is infinity array
target = 160

print(r.ans(myarr,target))