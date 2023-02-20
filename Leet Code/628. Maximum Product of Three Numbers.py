class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0] * nums[1] * nums[-1]
        b = nums[-1] * nums[-2] * nums[-3]

        if a > b:
            return a
        return b

#         nums.sort()


#         print(nums)

#         L = len(nums)

#         arr = []


#         for i in range(1,4):
#             arr.append(nums[-i])

#         print(arr)

#         ans = 1
#         for i in arr:

#             ans*=i
#         return ans



ans = Solution()
nums = [1,2,3]
print(ans.maximumProduct(nums))