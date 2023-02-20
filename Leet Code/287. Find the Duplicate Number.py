class Solution2:
    def findDuplicate(self, nums):

        nums.sort()

        for i in range(len(nums) - 1):

            if nums[i] == nums[i + 1]:
                return nums[i]

        return -1


# another method
class Solution3:

    def findDuplicate(self, nums):

        slow = nums[0]
        fast = nums[0]

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        fast = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


class Solution:

    def findDuplicate(self, nums):

        dummy = [0] * (len(nums) + 1)

        for i in nums:
            if dummy[i] == 0:
                dummy[i] += 1
            else:
                return i
        return -1


ans = Solution()
nums = [1,3,4,2,6,7,4]
print(ans.findDuplicate(nums))