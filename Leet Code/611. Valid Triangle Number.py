class Solution:
    def triangleNumber(self, nums):
        res = 0

        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            fix = nums[i]
            strt = 0
            end = i - 1

            while strt < end:
                if nums[strt] + nums[end] > fix:
                    res += end - strt
                    end -= 1
                else:
                    strt += 1

        return res

ans = Solution()

nums = [4,2,3,4]
print(ans.triangleNumber(nums))


