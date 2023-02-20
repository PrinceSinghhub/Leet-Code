class Solution:
    def find132pattern(self, nums):

        stack, mid_ele = [], float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < mid_ele:
                return True
            while stack and nums[i] > stack[-1]:
                mid_ele = stack.pop()
            stack.append(nums[i])
        return False


ans = Solution()
nums = [1,2,3,4]
print(ans.find132pattern(nums))