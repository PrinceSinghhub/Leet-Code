class Solution:
    def longestOnes(self, nums, k):

        start = 0
        end = 0
        n = len(nums)
        max_consecutive = 0

        while end < n:
            if nums[end] == 0:
                if k > 0:
                    k -= 1
                else:
                    max_consecutive = max(max_consecutive, end - start)
                    if nums[start] == 0:
                        k += 1
                    start += 1
                    continue
            end += 1
        return max(max_consecutive, end - start)


ans = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(ans.longestOnes(nums,k))