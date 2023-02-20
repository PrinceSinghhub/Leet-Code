class Solution:
    def moveZeroes(self, nums):


        start = 0
        end = len(nums)

        for i in range(start,end):

            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
                end-=1

        return nums

ans = Solution()
nums = [0,1,0,3,12]
print(ans.moveZeroes(nums))