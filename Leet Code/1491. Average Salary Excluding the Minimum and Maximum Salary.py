class Solution:
    def average(self, salary):

        salary.sort()
        L = len(salary)

        salary.remove(salary[0])
        salary.remove(salary[-1])

        Sum = sum(salary)

        return Sum / (L - 2)


ans = Solution()
arr = [6000,5000,4000,3000,2000,1000]
print(ans.average(arr))