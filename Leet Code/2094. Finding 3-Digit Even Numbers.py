from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits):
        ans = set()
        for x, y, z in permutations(digits, 3):
            if x != 0 and z & 1 == 0:
                ans.add(100*x + 10*y + z)
        return sorted(ans)


ans = Solution()
digits = [2,2,8,8,2]
print(ans.findEvenNumbers(digits))