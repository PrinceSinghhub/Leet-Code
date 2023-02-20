class Solution:
    def singleNonDuplicate(self, nums):
          l = 0
          r = len(nums)-1
          while l<r:
              mid = (l+r)//2
              if mid%2 != 0:
                      if nums[mid] == nums[mid+1]:
                          r = mid
                      else:
                          l = mid+1
              else:
                      if nums[mid] == nums[mid+1]:
                          l = mid+1
                      else:
                          r = mid
          return nums[l]


ans = Solution()
nums = [1,1,2,3,3,4,4,8,8]
print(ans.singleNonDuplicate(nums))