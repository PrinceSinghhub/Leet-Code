class Solution:
    def minSubArrayLen(self, target, nums):
        i, j = 0, 0
        count = 0
        maxi = 10 ** 5

        while j < len(nums):
            count += nums[j]

            if count == target:
                if maxi > (j - i + 1):
                    maxi = (j - i + 1)

                count -= nums[i]
                i += 1
                j += 1

            elif count > target:
                if maxi > (j - i + 1):
                    maxi = (j - i + 1)
                count -= nums[i]
                count -= nums[j]
                i += 1
            else:
                j += 1

        if maxi == 10 ** 5:
            return 0
        return maxi

ans = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(ans.minSubArrayLen(target,nums))