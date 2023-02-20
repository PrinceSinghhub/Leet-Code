class Solution:
    def sortEvenOdd(self, nums):

        n = len(nums)
        if n <= 2:
            return nums

        even = sorted([nums[i] for i in range(0, n, 2)])
        odd = sorted([nums[i] for i in range(1, n, 2)], reverse=True)

        res = []

        for i in range(len(even)):
            res.append(even[i])
            if i < len(odd):
                res.append(odd[i])

        return res


ans = Solution()
nums = [4,1,2,3]
print(ans.sortEvenOdd(nums))
