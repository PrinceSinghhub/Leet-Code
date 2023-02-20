import collections


class Solution:
    def subarraySum(self, nums, k):
        prefix = collections.Counter()
        current = 0

        prefix[current] = 1
        total = 0

        for x in nums:

            current += x
            prives = current - k

            if prives in prefix:
                total += prefix[prives]

            prefix[current] += 1

        return total

ans = Solution()
nums = [1,1,1]
k = 2
print(ans.subarraySum(nums,k))