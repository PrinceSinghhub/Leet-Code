# https://leetcode.com/problems/split-array-largest-sum/submissions/
class Solution:
    def splitArray(self, nums,m):

        start = 0
        end = 0

        for i in nums: #in the end that loop give a maximum value or array
            start = max(start,i)
            end+=i


        while(start<end):
            # try to find our middle as potiantial ans
             mid = start+(end-start)//2

             # calculate hwo MANY PICES you can divide this in with max sum
             sum = 0
             pices = 1

             for i in nums:
                 if(sum+i>mid):
                     sum = i
                     pices+=1
                 else:
                     sum+=i
             if pices>m:
                 start = mid+1
             else:
                 end = mid
        return end #we also return end becouse start and end are both are same at the end
ans = Solution()
nums = [7,2,5,10,8]; m = 2
print(ans.splitArray(nums,m))
