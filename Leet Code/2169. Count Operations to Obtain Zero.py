class Solution:
    def countOperations(self, num1, num2):

        count = 0

        while True:

            if num1 == 0 or num2 == 0:
                return count

            elif num1 >= num2:
                num1 = num1 - num2
                count += 1

            elif num2 > num1:
                num2 = num2 - num1
                count += 1
        return count

ans = Solution()
print(ans.countOperations(20,15))